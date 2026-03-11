from __future__ import annotations

import pytest

from storage_choice_basics import hybrid_needed, primary_storage, storage_tradeoff


def test_primary_storage_depends_on_access_pattern_and_transaction_need() -> None:
    assert primary_storage(needs_transactions=True, document_search=False, vector_similarity=False) == "relational"
    assert primary_storage(needs_transactions=False, document_search=True, vector_similarity=False) == "search"
    assert primary_storage(needs_transactions=False, document_search=False, vector_similarity=True) == "vector"
    assert primary_storage(needs_transactions=True, document_search=True, vector_similarity=False) == "hybrid"


def test_hybrid_needed_flags_multiple_competing_needs() -> None:
    assert hybrid_needed(needs_transactions=True, document_search=True, vector_similarity=False) is True
    assert hybrid_needed(needs_transactions=False, document_search=False, vector_similarity=True) is False


def test_storage_tradeoff_describes_primary_strength() -> None:
    assert storage_tradeoff("vector") == "approximate similarity search over embeddings"

    with pytest.raises(ValueError):
        storage_tradeoff("blob")
