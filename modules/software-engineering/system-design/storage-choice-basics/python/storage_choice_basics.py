from __future__ import annotations


def primary_storage(needs_transactions: bool, document_search: bool, vector_similarity: bool) -> str:
    if needs_transactions and not document_search and not vector_similarity:
        return "relational"
    if vector_similarity and not needs_transactions and not document_search:
        return "vector"
    if document_search and not needs_transactions and not vector_similarity:
        return "search"
    return "hybrid"


def hybrid_needed(needs_transactions: bool, document_search: bool, vector_similarity: bool) -> bool:
    return sum([needs_transactions, document_search, vector_similarity]) >= 2


def storage_tradeoff(storage: str) -> str:
    normalized_storage = storage.strip().lower()
    if normalized_storage == "relational":
        return "strong transactions and flexible query patterns"
    if normalized_storage == "search":
        return "text retrieval and ranking over document fields"
    if normalized_storage == "vector":
        return "approximate similarity search over embeddings"
    if normalized_storage == "hybrid":
        return "combine stores by access pattern and correctness need"
    raise ValueError("unknown storage")
