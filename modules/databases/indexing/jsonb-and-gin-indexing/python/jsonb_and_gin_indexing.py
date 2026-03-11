"""jsonb_and_gin_indexing - a tiny inverted index for JSON-like metadata."""

from __future__ import annotations


def metadata_terms(document: dict[str, object]) -> set[str]:
    metadata = document.get("metadata", {})
    assert isinstance(metadata, dict)
    terms: set[str] = set()
    for key, value in metadata.items():
        if isinstance(value, list):
            for item in value:
                terms.add(f"{key[:-1] if key.endswith('s') else key}={item}")
        else:
            terms.add(f"{key}={value}")
    return terms


def build_metadata_inverted_index(
    documents: list[dict[str, object]],
) -> dict[str, set[str]]:
    inverted: dict[str, set[str]] = {}
    for document in documents:
        doc_id = str(document["id"])
        for term in metadata_terms(document):
            inverted.setdefault(term, set()).add(doc_id)
    return inverted


def filter_documents_with_index(
    inverted_index: dict[str, set[str]],
    required_terms: list[str],
) -> list[str]:
    if not required_terms:
        return []
    postings = [inverted_index.get(term, set()) for term in required_terms]
    if not postings:
        return []
    return sorted(set.intersection(*postings))


def update_term_diff(
    previous_document: dict[str, object],
    new_document: dict[str, object],
) -> tuple[set[str], set[str]]:
    previous_terms = metadata_terms(previous_document)
    new_terms = metadata_terms(new_document)
    removed = previous_terms - new_terms
    added = new_terms - previous_terms
    return removed, added
