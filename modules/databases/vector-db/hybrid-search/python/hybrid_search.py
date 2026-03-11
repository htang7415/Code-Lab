"""hybrid_search - combine lexical overlap with cosine similarity."""

from __future__ import annotations

import math
import re


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


def cosine_similarity(left: list[float], right: list[float]) -> float:
    if len(left) != len(right):
        raise ValueError("vectors must have the same dimensions")
    left_norm = math.sqrt(sum(value * value for value in left))
    right_norm = math.sqrt(sum(value * value for value in right))
    if left_norm == 0 or right_norm == 0:
        return 0.0
    dot = sum(a * b for a, b in zip(left, right))
    similarity = dot / (left_norm * right_norm)
    if abs(similarity - 1.0) < 1e-12:
        return 1.0
    if abs(similarity + 1.0) < 1e-12:
        return -1.0
    return similarity


def lexical_overlap_score(query_text: str, doc_text: str) -> float:
    query_terms = set(tokenize(query_text))
    if not query_terms:
        return 0.0
    doc_terms = set(tokenize(doc_text))
    return len(query_terms & doc_terms) / len(query_terms)


def hybrid_score(
    query_text: str,
    query_vector: list[float],
    doc_text: str,
    doc_vector: list[float],
    alpha: float = 0.5,
) -> float:
    if not 0.0 <= alpha <= 1.0:
        raise ValueError("alpha must be between 0 and 1")
    semantic = cosine_similarity(query_vector, doc_vector)
    lexical = lexical_overlap_score(query_text, doc_text)
    return alpha * semantic + (1.0 - alpha) * lexical


def rank_documents(
    query_text: str,
    query_vector: list[float],
    documents: list[dict[str, object]],
    alpha: float = 0.5,
) -> list[tuple[str, float]]:
    scored = [
        (
            str(document["id"]),
            hybrid_score(
                query_text,
                query_vector,
                str(document["text"]),
                list(document["vector"]),
                alpha=alpha,
            ),
        )
        for document in documents
    ]
    return sorted(scored, key=lambda item: (-item[1], item[0]))
