"""Inferência local demonstrativa; não verifica a veracidade de fatos."""

from __future__ import annotations

import argparse
from pathlib import Path

import joblib

from news import normalize


def predict(path: Path, title: str, body: str) -> str:
    content = normalize(title + " " + body)
    if len(content) < 20:
        raise ValueError("Informe título e notícia com ao menos 20 caracteres")
    model = joblib.load(path)  # Aceite apenas artefatos gerados localmente.
    return str(model.predict([content])[0])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("title")
    parser.add_argument("body")
    parser.add_argument("--model", type=Path, default=Path("artifacts/model.joblib"))
    args = parser.parse_args()
    print("Rótulo previsto no padrão da base:", predict(args.model, args.title, args.body))
    print("Não confirma fatos. Verifique a notícia por fontes independentes.")

