from __future__ import annotations

import math
from collections import Counter


def tf_idf_weights(
    tokens: list[str],
    document_frequencies: dict[str, int],
    num_documents: int,
) -> dict[str, float]:
    if num_documents <= 0:
        raise ValueError("num_documents must be positive")
    if not tokens:
        return {}

    counts = Counter(tokens)
    total_tokens = len(tokens)
    weights: dict[str, float] = {}

    for term, count in counts.items():
        df = document_frequencies.get(term)
        if df is None:
            raise ValueError(f"missing document frequency for term {term!r}")
        if df <= 0 or df > num_documents:
            raise ValueError("document frequencies must be in [1, num_documents]")
        weights[term] = (count / total_tokens) * math.log(num_documents / df)

    return weights
