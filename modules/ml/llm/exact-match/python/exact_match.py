from __future__ import annotations

import re
import string


def _normalize_answer(text: str) -> str:
    text = text.lower()
    text = "".join(ch for ch in text if ch not in string.punctuation)
    text = re.sub(r"\b(a|an|the)\b", " ", text)
    return " ".join(text.split())


def exact_match_score(predictions: list[str], labels: list[str]) -> float:
    if len(predictions) != len(labels):
        raise ValueError("predictions and labels must have the same length")
    if not predictions:
        return 0.0

    matches = sum(
        _normalize_answer(prediction) == _normalize_answer(label)
        for prediction, label in zip(predictions, labels)
    )
    return matches / len(predictions)
