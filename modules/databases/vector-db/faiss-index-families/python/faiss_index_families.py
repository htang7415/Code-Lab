"""faiss_index_families - choose a FAISS family from workload constraints."""

from __future__ import annotations


_TARGET_RECALLS = {"baseline", "high"}
_MEMORY_TIERS = {"loose", "medium", "tight"}
_UPDATE_PATTERNS = {"online", "batch"}

_PROFILES = {
    "Flat": {
        "search": "exact",
        "strength": "best recall baseline",
        "weakness": "scores every vector",
    },
    "IVF": {
        "search": "approximate",
        "strength": "good large-corpus latency tradeoff",
        "weakness": "needs centroid and nprobe tuning",
    },
    "HNSW": {
        "search": "approximate",
        "strength": "strong recall with graph navigation",
        "weakness": "higher memory overhead",
    },
    "IVFPQ": {
        "search": "approximate",
        "strength": "saves substantial memory",
        "weakness": "extra compression error",
    },
}


def validate_choice_inputs(
    corpus_size: int,
    target_recall: str,
    memory_tier: str,
    update_pattern: str,
) -> None:
    if corpus_size <= 0:
        raise ValueError("corpus_size must be positive")
    if target_recall not in _TARGET_RECALLS:
        raise ValueError("target_recall must be 'baseline' or 'high'")
    if memory_tier not in _MEMORY_TIERS:
        raise ValueError("memory_tier must be 'loose', 'medium', or 'tight'")
    if update_pattern not in _UPDATE_PATTERNS:
        raise ValueError("update_pattern must be 'online' or 'batch'")


def faiss_family_profile(name: str) -> dict[str, str]:
    if name not in _PROFILES:
        raise ValueError(f"unknown FAISS family: {name}")
    return dict(_PROFILES[name])


def recommend_faiss_index(
    corpus_size: int,
    target_recall: str,
    memory_tier: str,
    update_pattern: str,
) -> str:
    validate_choice_inputs(corpus_size, target_recall, memory_tier, update_pattern)

    if corpus_size <= 100_000 and target_recall == "high" and memory_tier != "tight":
        return "Flat"
    if memory_tier == "tight":
        return "IVFPQ"
    if update_pattern == "online":
        return "HNSW"
    if corpus_size >= 1_000_000:
        return "IVF"
    if target_recall == "high":
        return "HNSW"
    return "IVF"
