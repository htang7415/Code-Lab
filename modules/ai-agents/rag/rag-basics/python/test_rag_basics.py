from __future__ import annotations

import pytest

from rag_basics import build_grounded_context, select_top_k


def test_rag_basics_selects_top_chunks_and_builds_context() -> None:
    chunks = [("A", 0.9), ("B", 0.7), ("C", 0.4)]
    top = select_top_k(chunks, k=2)
    assert top == ["A", "B"]
    context = build_grounded_context(top, max_chunks=2)
    assert context == "[1] A\n\n[2] B"


def test_rag_basics_validation_rejects_invalid_limits() -> None:
    with pytest.raises(ValueError):
        select_top_k([], k=0)
    with pytest.raises(ValueError):
        build_grounded_context(["A"], max_chunks=0)
