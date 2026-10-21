"""Offline CSV -> validated SQLite -> SQL summaries -> charts."""
import csv
import hashlib
import json
import sqlite3
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load_database(source=ROOT / "data/day.csv"):
    expected = json.loads((ROOT / "data/source.json").read_text())["day_csv_sha256"]
    if hashlib.sha256(source.read_bytes()).hexdigest() != expected:
        raise ValueError("Dataset checksum differs from the documented source.")
    with source.open(newline="") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
    required = ["instant", "dteday", "season", "yr", "mnth", "holiday", "weekday",
                "workingday", "weathersit", "temp", "atemp", "hum", "windspeed",
                "casual", "registered", "cnt"]
    if reader.fieldnames != required or len(rows) != 731:
        raise ValueError("Unexpected schema or daily row count.")
    expected_dates = [(date(2011, 1, 1) + timedelta(days=i)).isoformat() for i in range(731)]
    if [r["dteday"] for r in rows] != expected_dates:
        raise ValueError("Dates must cover every day of 2011 and 2012 exactly once, in order.")
    for row in rows:
        day = date.fromisoformat(row["dteday"])
        if int(row["yr"]) != day.year - 2011 or int(row["mnth"]) != day.month:
            raise ValueError("Date and year/month columns disagree.")
        if int(row["weekday"]) != (day.weekday() + 1) % 7:
            raise ValueError("Date and weekday disagree.")
        if int(row["workingday"]) != int(day.weekday() < 5 and int(row["holiday"]) == 0):
            raise ValueError("Working-day flag disagrees with weekday/holiday.")
    connection = sqlite3.connect(":memory:")
    connection.row_factory = sqlite3.Row
    connection.executescript((ROOT / "sql/schema.sql").read_text())
    connection.executemany(
        "INSERT INTO daily_rentals VALUES (" + ",".join(["?"] * len(required)) + ")",
        [[r[col] for col in required] for r in rows],
    )
    return connection


def query(connection, name):
    return [dict(row) for row in connection.execute((ROOT / "sql" / (name + ".sql")).read_text())]


def main():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    matplotlib.rcParams["svg.hashsalt"] = "bike-demand-v1"
    matplotlib.rcParams["svg.fonttype"] = "none"
    output = ROOT / "outputs"
    output.mkdir(exist_ok=True)
    with load_database() as connection:
        summaries = {name: query(connection, name) for name in ["annual", "monthly", "segments", "weather"]}
    for name, rows in summaries.items():
        with (output / (name + ".csv")).open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
    annual = summaries["annual"]
    growth = 100 * (annual[1]["mean_daily_rentals"] / annual[0]["mean_daily_rentals"] - 1)
    metrics = {"rows": 731, "date_start": "2011-01-01", "date_end": "2012-12-31",
               "annual": annual, "mean_daily_growth_pct": round(growth, 2)}
    (output / "metrics.json").write_text(json.dumps(metrics, indent=2) + "\n")
    fig, ax = plt.subplots(figsize=(10, 4.8), layout="constrained")
    for year, color in [("2011", "#2563eb"), ("2012", "#c2410c")]:
        rows = [r for r in summaries["monthly"] if r["month"].startswith(year)]
        ax.plot(range(1, 13), [r["mean_daily_rentals"] for r in rows], marker="o", label=year, color=color)
    ax.set(title="Bike rentals rose in 2012; daily volume varied by month",
           xlabel="Month", ylabel="Mean rentals per day", xticks=range(1, 13), ylim=(0, 8000))
    ax.legend(title="Observed year");ax.grid(axis="y", alpha=0.2)
    fig.savefig(output / "monthly.svg", metadata={"Date": None})
    plt.close(fig)
    fig, ax = plt.subplots(figsize=(10, 5.2), layout="constrained")
    rows = summaries["segments"]
    labels = [str(r["year"]) + "\n" + r["day_type"] for r in rows]
    ax.bar(labels, [r["mean_registered"] for r in rows], label="Registered", color="#2563eb")
    ax.bar(labels, [r["mean_casual"] for r in rows], bottom=[r["mean_registered"] for r in rows],
           label="Casual", color="#c2410c")
    ax.set(title="Rider mix differs between working days and weekends/holidays",
           ylabel="Mean rentals per day", ylim=(0, 7000))
    ax.legend();ax.grid(axis="y", alpha=0.2)
    fig.savefig(output / "segments.svg", metadata={"Date": None})
    plt.close(fig)
    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
