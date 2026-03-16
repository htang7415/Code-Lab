from __future__ import annotations

import pytest

from faiss_index_families import faiss_family_profile, recommend_faiss_index


def test_recommend_faiss_index_prefers_flat_for_small_high_recall_workloads() -> None:
    assert recommend_faiss_index(50_000, "high", "medium", "batch") == "Flat"


def test_recommend_faiss_index_prefers_ivfpq_when_memory_is_tight() -> None:
    assert recommend_faiss_index(5_000_000, "baseline", "tight", "batch") == "IVFPQ"


def test_recommend_faiss_index_prefers_hnsw_for_online_updates() -> None:
    assert recommend_faiss_index(500_000, "high", "medium", "online") == "HNSW"


def test_faiss_family_profile_and_invalid_inputs_are_checked() -> None:
    assert faiss_family_profile("IVF")["search"] == "approximate"

    with pytest.raises(ValueError, match="target_recall"):
        recommend_faiss_index(100_000, "max", "medium", "batch")
