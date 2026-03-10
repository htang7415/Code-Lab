from __future__ import annotations

import re
import string


def _normalize_answer(text: str) -> str:
    text = text.lower()
    text = "".join(character for character in text if character not in string.punctuation)
    text = re.sub(r"\b(a|an|the)\b", " ", text)
    return " ".join(text.split())


def minority_cluster_tail_gap(answers: list[str]) -> float:
    if not answers:
        return 0.0

    counts: dict[str, int] = {}
    for answer in answers:
        normalized = _normalize_answer(answer)
        counts[normalized] = counts.get(normalized, 0) + 1

    tail_sizes = sorted(counts.values(), reverse=True)[2:]
    if not tail_sizes:
        return 0.0

    tail_total = sum(tail_sizes)
    top_share = max(tail_sizes) / tail_total
    second_share = 0.0
    if len(tail_sizes) > 1:
        second_share = sorted(tail_sizes, reverse=True)[1] / tail_total
    return top_share - second_share
