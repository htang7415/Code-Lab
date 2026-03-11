"""reranking_pipelines - candidate retrieval followed by a stronger reranker."""

from __future__ import annotations

import re


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


def initial_retrieve(
    documents: list[dict[str, object]],
    candidate_k: int,
) -> list[dict[str, object]]:
    ranked = sorted(
        documents,
        key=lambda document: (-float(document["retrieval_score"]), str(document["id"])),
    )
    return ranked[:candidate_k]


def rerank_score(query_text: str, document: dict[str, object]) -> float:
    query_tokens = set(tokenize(query_text))
    doc_text = str(document["text"])
    doc_tokens = set(tokenize(doc_text))
    overlap = 0.0 if not query_tokens else len(query_tokens & doc_tokens) / len(query_tokens)
    exact_phrase_bonus = 1.0 if query_text.lower() in doc_text.lower() else 0.0
    retrieval_score = float(document["retrieval_score"])
    return 0.2 * retrieval_score + 0.5 * overlap + 0.3 * exact_phrase_bonus


def rerank_candidates(
    query_text: str,
    candidates: list[dict[str, object]],
) -> list[tuple[str, float]]:
    scored = [
        (str(document["id"]), rerank_score(query_text, document))
        for document in candidates
    ]
    return sorted(scored, key=lambda item: (-item[1], item[0]))


def pipeline_rank(
    query_text: str,
    documents: list[dict[str, object]],
    candidate_k: int,
    final_k: int,
) -> list[str]:
    candidates = initial_retrieve(documents, candidate_k=candidate_k)
    reranked = rerank_candidates(query_text, candidates)
    return [doc_id for doc_id, _ in reranked[:final_k]]
