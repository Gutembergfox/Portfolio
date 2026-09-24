import tempfile
import unittest
from pathlib import Path

import pandas as pd

from app import predict
from model import clean_text, prepare_data, split_data
from train import run


class ProjectTests(unittest.TestCase):
    def test_clean_removes_explicit_label_and_url(self):
        self.assertEqual(clean_text("Sou INTP ||| veja https://example.org/a agora"),
                         "Sou veja agora")

    def test_schema_and_duplicates(self):
        with self.assertRaises(ValueError):
            prepare_data(pd.DataFrame({"texto": ["x"]}))
        frame = pd.DataFrame({"type": ["intp", "intp", "XXXX"],
                              "posts": ["um texto bastante longo de teste"] * 3})
        self.assertEqual(len(prepare_data(frame)), 1)

    def test_train_evaluate_and_predict(self):
        rows = []
        for index in range(20):
            rows.append({"type": "INTP" if index % 2 else "ENFJ",
                         "posts": f"registro {index} com palavras suficientes para análise de texto"})
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            csv = directory / "fixture.csv"
            pd.DataFrame(rows).to_csv(csv, index=False)
            prepared = prepare_data(pd.read_csv(csv))
            x_train, x_test, _, _ = split_data(prepared)
            self.assertFalse(set(x_train) & set(x_test))
            results = run(csv, directory / "artifacts")
            self.assertEqual(results["test_rows"], 4)
            self.assertTrue((directory / "artifacts/metrics.json").exists())
            prediction = predict(directory / "artifacts/model.joblib",
                                 "este é um texto novo suficientemente extenso para teste")
            self.assertIn(prediction, {"INTP", "ENFJ"})


if __name__ == "__main__":
    unittest.main()

