from __future__ import annotations

import re
import string


def _normalize_answer(text: str) -> str:
    text = text.lower()
    text = "".join(character for character in text if character not in string.punctuation)
    text = re.sub(r"\b(a|an|the)\b", " ", text)
    return " ".join(text.split())


def minority_cluster_remainder_ratio(answers: list[str]) -> float:
    if not answers:
        return 0.0

    counts: dict[str, int] = {}
    for answer in answers:
        normalized = _normalize_answer(answer)
        counts[normalized] = counts.get(normalized, 0) + 1

    minority_sizes = sorted(counts.values(), reverse=True)[1:]
    if not minority_sizes:
        return 0.0

    minority_total = sum(minority_sizes)
    residual_count = minority_total - max(minority_sizes)
    return residual_count / minority_total
