from __future__ import annotations

import math
import re
from collections import Counter


def _tokens(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


def bleu1_meteor(
    candidate: str,
    reference: str,
) -> tuple[float, float]:
    candidate_tokens = _tokens(candidate)
    reference_tokens = _tokens(reference)
    if not candidate_tokens or not reference_tokens:
        raise ValueError("candidate and reference must contain at least one token")

    candidate_counts = Counter(candidate_tokens)
    reference_counts = Counter(reference_tokens)
    matches = sum(
        min(count, reference_counts[token]) for token, count in candidate_counts.items()
    )

    precision = matches / len(candidate_tokens)
    recall = matches / len(reference_tokens)

    brevity_penalty = 1.0
    if len(candidate_tokens) < len(reference_tokens):
        brevity_penalty = math.exp(1.0 - len(reference_tokens) / len(candidate_tokens))
    bleu1 = brevity_penalty * precision

    if precision == 0.0 or recall == 0.0:
        meteor = 0.0
    else:
        meteor = (10.0 * precision * recall) / (recall + 9.0 * precision)

    return bleu1, meteor
