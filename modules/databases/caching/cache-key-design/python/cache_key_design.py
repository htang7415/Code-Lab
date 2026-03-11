"""cache_key_design - stable scoped keys prevent silent cache collisions."""

from __future__ import annotations


def cache_key(
    namespace: str,
    workspace_id: int,
    resource_id: str,
    version: str,
    extras: dict[str, object] | None = None,
) -> str:
    parts = [
        namespace,
        f"ws={workspace_id}",
        f"id={resource_id}",
        f"v={version}",
    ]
    if extras:
        parts.extend(
            f"{key}={extras[key]}"
            for key in sorted(extras)
        )
    return "|".join(parts)


def parse_cache_key(key: str) -> dict[str, object]:
    pieces = key.split("|")
    parsed: dict[str, object] = {"namespace": pieces[0]}
    for piece in pieces[1:]:
        field, value = piece.split("=", 1)
        parsed[field] = int(value) if field == "ws" else value
    return parsed


def naive_key(resource_id: str) -> str:
    return resource_id


def key_collides(left: str, right: str) -> bool:
    return left == right
