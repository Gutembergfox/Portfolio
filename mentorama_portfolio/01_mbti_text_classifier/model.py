"""Preparação de textos e treinamento para uma demonstração de classificação MBTI."""

from __future__ import annotations

import re

import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

VALID_TYPES = {
    a + b + c + d
    for a in "IE" for b in "NS" for c in "TF" for d in "JP"
}
_URL = re.compile(r"https?://\S+|www\.\S+", flags=re.IGNORECASE)
_LABEL = re.compile(r"\b(?:" + "|".join(sorted(VALID_TYPES)) + r")\b", re.IGNORECASE)


def clean_text(value: str) -> str:
    """Remove URLs and explicit MBTI labels to limit trivial target leakage."""
    if not isinstance(value, str):
        raise TypeError("O texto deve ser uma string")
    value = _URL.sub(" ", value)
    value = _LABEL.sub(" ", value)
    return " ".join(value.replace("|||", " ").split())


def prepare_data(frame: pd.DataFrame) -> pd.DataFrame:
    if not {"type", "posts"}.issubset(frame.columns):
        raise ValueError("O CSV deve conter as colunas 'type' e 'posts'")
    result = frame[["type", "posts"]].dropna().copy()
    result["type"] = result["type"].astype(str).str.upper().str.strip()
    result = result[result["type"].isin(VALID_TYPES)].copy()
    result["posts"] = result["posts"].map(clean_text)
    result = result[result["posts"].str.len() >= 20]
    # Duplicatas exatas entre treino e teste podem inflar artificialmente as métricas.
    return result.drop_duplicates(subset=["posts"]).reset_index(drop=True)


def split_data(frame: pd.DataFrame, seed: int = 42):
    if len(frame) < 4 or frame["type"].nunique() < 2:
        raise ValueError("São necessários ao menos quatro textos e duas classes")
    counts = frame["type"].value_counts()
    test_count = max(1, round(len(frame) * 0.2))
    stratify = frame["type"] if counts.min() >= 2 and test_count >= len(counts) else None
    return train_test_split(
        frame["posts"], frame["type"], test_size=0.2,
        random_state=seed, stratify=stratify,
    )


def make_pipeline() -> Pipeline:
    return Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=1,
                                   max_features=50_000, sublinear_tf=True)),
        ("classifier", LogisticRegression(max_iter=1000, class_weight="balanced")),
    ])


def make_baseline() -> Pipeline:
    return Pipeline([
        ("tfidf", TfidfVectorizer(min_df=1, max_features=50_000)),
        ("classifier", DummyClassifier(strategy="most_frequent")),
    ])

