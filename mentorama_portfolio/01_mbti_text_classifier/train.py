"""Treina e avalia o classificador em um conjunto de teste reservado."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, f1_score

from model import make_baseline, make_pipeline, prepare_data, split_data


def run(csv_path: Path, output: Path, seed: int = 42) -> dict:
    frame = prepare_data(pd.read_csv(csv_path))
    x_train, x_test, y_train, y_test = split_data(frame, seed)
    results = {"rows": len(frame), "train_rows": len(x_train),
               "test_rows": len(x_test), "seed": seed,
               "class_counts": frame["type"].value_counts().to_dict()}
    for name, model in (("baseline", make_baseline()), ("tfidf_logistic", make_pipeline())):
        model.fit(x_train, y_train)
        pred = model.predict(x_test)
        results[name] = {
            "accuracy": accuracy_score(y_test, pred),
            "macro_f1": f1_score(y_test, pred, average="macro", zero_division=0),
            "per_class": classification_report(y_test, pred, output_dict=True,
                                               zero_division=0),
        }
        if name == "tfidf_logistic":
            output.mkdir(parents=True, exist_ok=True)
            joblib.dump(model, output / "model.joblib")
    (output / "metrics.json").write_text(
        json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", type=Path, help="CSV com colunas type e posts")
    parser.add_argument("--output", type=Path, default=Path("artifacts"))
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    metrics = run(args.csv, args.output, args.seed)
    print(json.dumps({k: v for k, v in metrics.items() if k != "class_counts"},
                     ensure_ascii=False, indent=2))

