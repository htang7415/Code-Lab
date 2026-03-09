from __future__ import annotations

import re
import string


def _normalize_answer(text: str) -> str:
    text = text.lower()
    text = "".join(character for character in text if character not in string.punctuation)
    text = re.sub(r"\b(a|an|the)\b", " ", text)
    return " ".join(text.split())


def minority_cluster_mode(answers: list[str]) -> int:
    if not answers:
        return 0

    counts: dict[str, int] = {}
    for answer in answers:
        normalized = _normalize_answer(answer)
        counts[normalized] = counts.get(normalized, 0) + 1

    cluster_sizes = sorted(counts.values(), reverse=True)
    minority_sizes = cluster_sizes[1:]
    if not minority_sizes:
        return 0

    size_counts: dict[int, int] = {}
    for size in minority_sizes:
        size_counts[size] = size_counts.get(size, 0) + 1
    return max(size_counts, key=lambda size: (size_counts[size], size))
