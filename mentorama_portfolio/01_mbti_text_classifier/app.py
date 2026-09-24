"""Demonstração local por terminal. Entrada: texto de autoria voluntária."""

from __future__ import annotations

import argparse
from pathlib import Path

import joblib

from model import clean_text


def predict(model_path: Path, text: str) -> str:
    cleaned = clean_text(text)
    if len(cleaned) < 20:
        raise ValueError("Informe ao menos 20 caracteres de texto após a limpeza")
    model = joblib.load(model_path)  # Carregue somente artefatos gerados por você.
    return str(model.predict([cleaned])[0])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("text", help="Texto a classificar")
    parser.add_argument("--model", type=Path, default=Path("artifacts/model.joblib"))
    args = parser.parse_args()
    print("Classe prevista:", predict(args.model, args.text))
    print("Demonstração experimental; não é avaliação psicológica e não deve ser usada para seleção de pessoas.")

