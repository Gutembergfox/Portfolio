import tempfile
import unittest
from pathlib import Path

import pandas as pd

from app import predict
from news import prepare, split
from train import run


class NewsTests(unittest.TestCase):
    def test_schema_and_conflicting_duplicates(self):
        with self.assertRaises(ValueError):
            prepare(pd.DataFrame({"body": ["a"]}))
        rows = pd.DataFrame({"title": ["mesmo", "mesmo"],
                             "text": ["texto longo sem alteracao"] * 2,
                             "label": ["fake", "real"]})
        with self.assertRaises(ValueError):
            prepare(rows)

    def test_train_and_inference(self):
        rows = [{"title": f"título {i}",
                 "text": f"corpo suficientemente longo e único para a amostra número {i}",
                 "label": "fake" if i % 2 else "real"}
                for i in range(20)]
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            csv = root / "fixture.csv"
            pd.DataFrame(rows).to_csv(csv, index=False)
            x_train, x_test, _, _ = split(prepare(pd.read_csv(csv)))
            self.assertFalse(set(x_train) & set(x_test))
            metrics = run(csv, root / "out")
            self.assertEqual(metrics["test_rows"], 4)
            self.assertIn(predict(root / "out/model.joblib", "Notícia de exemplo",
                                  "Um corpo suficiente para exercer a inferência."),
                          {"fake", "real"})


if __name__ == "__main__":
    unittest.main()

