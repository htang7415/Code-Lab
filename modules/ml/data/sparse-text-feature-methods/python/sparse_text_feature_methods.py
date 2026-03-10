from __future__ import annotations

import hashlib
import math
from collections import Counter


def count_vector(tokens: list[str], vocabulary: list[str]) -> list[int]:
    if len(set(vocabulary)) != len(vocabulary):
        raise ValueError("vocabulary must contain unique terms")
    counts = Counter(tokens)
    return [counts.get(term, 0) for term in vocabulary]


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


def _stable_bucket(token: str, num_buckets: int) -> int:
    digest = hashlib.md5(token.encode("utf-8")).digest()
    return int.from_bytes(digest[:8], byteorder="big") % num_buckets


def hashed_feature_counts(tokens: list[str], num_buckets: int) -> list[int]:
    if num_buckets <= 0:
        raise ValueError("num_buckets must be positive")

    counts = [0] * num_buckets
    for token in tokens:
        counts[_stable_bucket(token, num_buckets)] += 1
    return counts


def chi_square_feature_score(
    present_positive: int,
    present_negative: int,
    absent_positive: int,
    absent_negative: int,
) -> float:
    counts = [present_positive, present_negative, absent_positive, absent_negative]
    if any(count < 0 for count in counts):
        raise ValueError("counts must be non-negative")

    total = sum(counts)
    if total == 0:
        return 0.0

    present_total = present_positive + present_negative
    absent_total = absent_positive + absent_negative
    positive_total = present_positive + absent_positive
    negative_total = present_negative + absent_negative

    observed = [present_positive, present_negative, absent_positive, absent_negative]
    expected = [
        present_total * positive_total / total,
        present_total * negative_total / total,
        absent_total * positive_total / total,
        absent_total * negative_total / total,
    ]

    score = 0.0
    for observed_count, expected_count in zip(observed, expected):
        if expected_count > 0.0:
            score += (observed_count - expected_count) ** 2 / expected_count
    return score


def prune_rare_tokens(tokens: list[str], min_count: int, unk_token: str = "__UNK__") -> list[str]:
    if min_count <= 0:
        raise ValueError("min_count must be positive")

    counts: dict[str, int] = {}
    for token in tokens:
        counts[token] = counts.get(token, 0) + 1

    return [token if counts[token] >= min_count else unk_token for token in tokens]
