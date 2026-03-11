"""semantic_cache_invalidation - version-aware semantic cache invalidation."""

from __future__ import annotations

import re


def validate_lookup_inputs(similarity_threshold: float, max_age_seconds: int) -> None:
    if not 0.0 <= similarity_threshold <= 1.0:
        raise ValueError("similarity_threshold must be between 0 and 1")
    if max_age_seconds < 0:
        raise ValueError("max_age_seconds must be non-negative")


def token_overlap_score(left: str, right: str) -> float:
    left_tokens = set(re.findall(r"[a-z0-9]+", left.lower()))
    right_tokens = set(re.findall(r"[a-z0-9]+", right.lower()))
    if not left_tokens:
        return 0.0
    return len(left_tokens & right_tokens) / len(left_tokens)


def store_semantic_entry(
    entries: list[dict[str, object]],
    query: str,
    response: str,
    workspace_id: int,
    policy_version: str,
    source_version: str,
    now: int,
) -> None:
    entries.append(
        {
            "query": query,
            "response": response,
            "workspace_id": workspace_id,
            "policy_version": policy_version,
            "source_version": source_version,
            "created_at": now,
        }
    )


def lookup_semantic_cache(
    entries: list[dict[str, object]],
    query: str,
    workspace_id: int,
    policy_version: str,
    source_version: str,
    now: int,
    similarity_threshold: float = 0.5,
    max_age_seconds: int = 300,
) -> str | None:
    validate_lookup_inputs(similarity_threshold, max_age_seconds)
    best_match: tuple[float, int, str] | None = None
    for entry in entries:
        if int(entry["workspace_id"]) != workspace_id:
            continue
        if entry["policy_version"] != policy_version:
            continue
        if entry["source_version"] != source_version:
            continue
        age = now - int(entry["created_at"])
        if age > max_age_seconds:
            continue
        score = token_overlap_score(query, str(entry["query"]))
        if score < similarity_threshold:
            continue
        created_at = int(entry["created_at"])
        response = str(entry["response"])
        if best_match is None or (score, created_at) > (best_match[0], best_match[1]):
            best_match = (score, created_at, response)
    return None if best_match is None else best_match[2]


def invalidate_scope(
    entries: list[dict[str, object]],
    workspace_id: int,
    current_policy_version: str,
    current_source_version: str,
) -> int:
    before = len(entries)
    entries[:] = [
        entry
        for entry in entries
        if int(entry["workspace_id"]) != workspace_id
        or (
            entry["policy_version"] == current_policy_version
            and entry["source_version"] == current_source_version
        )
    ]
    return before - len(entries)
