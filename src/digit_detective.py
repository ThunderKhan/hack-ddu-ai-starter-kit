"""Reproducible handwritten digit classification starter.

Uses the built-in scikit-learn digits dataset: no downloads or API credentials.
Participants should change and measure the baseline, not submit it unchanged.
"""
from __future__ import annotations

import numpy as np
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def train_digit_model(random_state: int = 42) -> dict:
    """Train on 75% of examples and evaluate once on untouched 25% test data."""
    digits = load_digits()
    x_train, x_test, y_train, y_test = train_test_split(
        digits.data, digits.target, test_size=0.25,
        random_state=random_state, stratify=digits.target,
    )
    model = make_pipeline(
        StandardScaler(),
        LogisticRegression(max_iter=2000, random_state=random_state),
    )
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    return {
        "model": model,
        "x_train": x_train, "x_test": x_test,
        "y_train": y_train, "y_test": y_test,
        "predictions": predictions,
        "accuracy": float(accuracy_score(y_test, predictions)),
        "report": classification_report(y_test, predictions, zero_division=0),
        "confusion_matrix": confusion_matrix(y_test, predictions),
    }


def predict_digit(model, pixels) -> dict:
    """Predict a digit from exactly 64 grayscale feature values (8x8 image)."""
    array = np.asarray(pixels, dtype=float)
    if array.size != 64 or not np.all(np.isfinite(array)):
        raise ValueError("Expected exactly 64 finite grayscale values.")
    if np.any(array < 0) or np.any(array > 16):
        raise ValueError("Built-in digits images use values from 0 to 16.")
    probabilities = model.predict_proba(array.reshape(1, 64))[0]
    best = int(np.argmax(probabilities))
    return {
        "digit": int(model.classes_[best]),
        "confidence": float(probabilities[best]),
        "probabilities": probabilities.tolist(),
    }
