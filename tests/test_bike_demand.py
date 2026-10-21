import csv
import importlib.util
import sqlite3
import tempfile
import unittest
from pathlib import Path

path = Path(__file__).parents[1] / "projects/bike_demand/run.py"
spec = importlib.util.spec_from_file_location("bike_demand", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class BikeDemandTests(unittest.TestCase):
    def test_dates_totals_and_sql_agree_with_independent_csv_aggregation(self):
        with (module.ROOT / "data/day.csv").open() as handle:
            rows = list(csv.DictReader(handle))
        with module.load_database() as db:
            annual = module.query(db, "annual")
            self.assertEqual(db.execute("SELECT COUNT(*) FROM daily_rentals").fetchone()[0], 731)
            for result in annual:
                subset = [r for r in rows if r["dteday"].startswith(str(result["year"]))]
                self.assertEqual(result["rentals"], sum(int(r["cnt"]) for r in subset))
                self.assertEqual(result["days"], len(subset))
                self.assertAlmostEqual(result["mean_daily_rentals"], sum(int(r["cnt"]) for r in subset) / len(subset), places=2)
            self.assertEqual(sum(r["rentals"] for r in module.query(db, "monthly")), sum(r["rentals"] for r in annual))

    def test_constraints_reject_inconsistent_total(self):
        with module.load_database() as db:
            with self.assertRaises(sqlite3.IntegrityError):
                db.execute("UPDATE daily_rentals SET cnt = cnt + 1 WHERE instant = 1")

    def test_modified_source_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            altered = Path(directory) / "day.csv"
            altered.write_bytes((module.ROOT / "data/day.csv").read_bytes() + b"\n")
            with self.assertRaisesRegex(ValueError, "checksum"):
                module.load_database(altered)
