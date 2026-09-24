"""Treinamento com teste reservado e comparação a uma classe majoritária."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, f1_score

from news import classifiers, prepare, split


def run(csv: Path, output: Path, seed: int = 42) -> dict:
    data = prepare(pd.read_csv(csv))
    x_train, x_test, y_train, y_test = split(data, seed)
    metrics = {"rows": len(data), "train_rows": len(x_train),
               "test_rows": len(x_test), "seed": seed,
               "class_counts": data["label"].value_counts().to_dict()}
    output.mkdir(parents=True, exist_ok=True)
    for name, model in classifiers().items():
        model.fit(x_train, y_train)
        pred = model.predict(x_test)
        metrics[name] = {
            "accuracy": accuracy_score(y_test, pred),
            "macro_f1": f1_score(y_test, pred, average="macro", zero_division=0),
            "per_class": classification_report(y_test, pred, output_dict=True,
                                               zero_division=0),
        }
        if name == "tfidf_logistic":
            joblib.dump(model, output / "model.joblib")
    (output / "metrics.json").write_text(
        json.dumps(metrics, indent=2, ensure_ascii=False), encoding="utf-8")
    return metrics


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", type=Path)
    parser.add_argument("--output", type=Path, default=Path("artifacts"))
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    print(json.dumps(run(args.csv, args.output, args.seed), indent=2,
                     ensure_ascii=False))

