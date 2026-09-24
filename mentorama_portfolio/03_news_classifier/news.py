"""Pipeline supervisionado para distinguir rótulos de notícias em uma base específica."""

from __future__ import annotations

import re

import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

_SPACE = re.compile(r"\s+")
_LABELS = {"fake": "fake", "false": "fake", "falsa": "fake",
           "real": "real", "true": "real", "verdadeira": "real"}


def normalize(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Texto inválido")
    return _SPACE.sub(" ", text).strip()


def prepare(frame: pd.DataFrame) -> pd.DataFrame:
    required = {"title", "text", "label"}
    if not required.issubset(frame.columns):
        raise ValueError("CSV precisa de title, text e label; id é opcional")
    data = frame[["title", "text", "label"]].dropna().copy()
    data["label"] = data["label"].astype(str).str.strip().str.lower().map(_LABELS)
    if data["label"].isna().any():
        raise ValueError("Rótulos aceitos: fake/real, false/true, falsa/verdadeira")
    data["content"] = (data["title"].astype(str) + " " + data["text"].astype(str)).map(normalize)
    data = data[data["content"].str.len() >= 20]
    # Uma notícia idêntica com rótulos opostos indica inconsistência dos dados.
    if data.groupby("content")["label"].nunique().gt(1).any():
        raise ValueError("Mesmo texto aparece com rótulos contraditórios")
    return data[["content", "label"]].drop_duplicates("content").reset_index(drop=True)


def split(data: pd.DataFrame, seed: int = 42):
    counts = data["label"].value_counts()
    if len(counts) != 2 or counts.min() < 2:
        raise ValueError("Cada classe requer pelo menos dois exemplos")
    return train_test_split(data["content"], data["label"],
                            test_size=0.2, random_state=seed,
                            stratify=data["label"] if len(data) >= 10 else None)


def classifiers():
    vectorizer = lambda: TfidfVectorizer(ngram_range=(1, 2), max_features=50_000,
                                         min_df=1, sublinear_tf=True)
    return {
        "baseline": Pipeline([("tfidf", vectorizer()),
                              ("classifier", DummyClassifier(strategy="most_frequent"))]),
        "tfidf_logistic": Pipeline([("tfidf", vectorizer()),
                                   ("classifier", LogisticRegression(max_iter=1000,
                                                                     class_weight="balanced"))]),
    }
