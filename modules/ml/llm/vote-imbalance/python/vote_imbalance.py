from __future__ import annotations

import re
import string


def _normalize_answer(text: str) -> str:
    text = text.lower()
    text = "".join(character for character in text if character not in string.punctuation)
    text = re.sub(r"\b(a|an|the)\b", " ", text)
    return " ".join(text.split())


def vote_imbalance(answers: list[str]) -> float:
    if not answers:
        return 0.0

    counts: dict[str, int] = {}
    for answer in answers:
        normalized = _normalize_answer(answer)
        counts[normalized] = counts.get(normalized, 0) + 1

    sorted_counts = sorted(counts.values(), reverse=True)
    if len(sorted_counts) == 1:
        return 1.0
    top, runner_up = sorted_counts[0], sorted_counts[1]
    return (top - runner_up) / (top + runner_up)
