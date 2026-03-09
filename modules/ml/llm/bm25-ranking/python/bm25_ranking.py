from __future__ import annotations

import math
from collections import Counter


def bm25_score(
    query_terms: list[str],
    document_terms: list[str],
    document_frequencies: dict[str, int],
    num_documents: int,
    avg_doc_length: float,
    k1: float = 1.5,
    b: float = 0.75,
) -> float:
    if num_documents <= 0:
        raise ValueError("num_documents must be positive")
    if avg_doc_length <= 0.0:
        raise ValueError("avg_doc_length must be positive")
    if k1 < 0.0:
        raise ValueError("k1 must be non-negative")
    if not 0.0 <= b <= 1.0:
        raise ValueError("b must satisfy 0 <= b <= 1")
    if not query_terms or not document_terms:
        return 0.0

    term_counts = Counter(document_terms)
    doc_length = len(document_terms)
    score = 0.0

    for term in query_terms:
        tf = term_counts.get(term, 0)
        if tf == 0:
            continue
        df = document_frequencies.get(term)
        if df is None:
            raise ValueError(f"missing document frequency for term {term!r}")
        if df <= 0 or df > num_documents:
            raise ValueError("document frequencies must be in [1, num_documents]")

        idf = math.log(1.0 + (num_documents - df + 0.5) / (df + 0.5))
        norm = tf + k1 * (1.0 - b + b * doc_length / avg_doc_length)
        score += idf * (tf * (k1 + 1.0)) / norm

    return score
