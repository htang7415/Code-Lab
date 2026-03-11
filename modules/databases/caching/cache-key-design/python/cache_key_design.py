"""cache_key_design - stable scoped keys prevent silent cache collisions."""

from __future__ import annotations


def validate_key_fragment(name: str, value: str) -> None:
    if value == "":
        raise ValueError(f"{name} must not be empty")
    if "|" in value or "=" in value:
        raise ValueError(f"{name} must not contain '|' or '='")


def cache_key(
    namespace: str,
    workspace_id: int,
    resource_id: str,
    version: str,
    extras: dict[str, object] | None = None,
) -> str:
    if workspace_id < 0:
        raise ValueError("workspace_id must be non-negative")
    validate_key_fragment("namespace", namespace)
    validate_key_fragment("resource_id", resource_id)
    validate_key_fragment("version", version)
    parts = [
        namespace,
        f"ws={workspace_id}",
        f"id={resource_id}",
        f"v={version}",
    ]
    if extras:
        for key, value in extras.items():
            validate_key_fragment("extra key", key)
            validate_key_fragment(f"extra value for {key}", str(value))
        parts.extend(
            f"{key}={extras[key]}"
            for key in sorted(extras)
        )
    return "|".join(parts)


def parse_cache_key(key: str) -> dict[str, object]:
    pieces = key.split("|")
    if not pieces or pieces[0] == "":
        raise ValueError("key must include a namespace")
    parsed: dict[str, object] = {"namespace": pieces[0]}
    for piece in pieces[1:]:
        if "=" not in piece:
            raise ValueError("key pieces must contain '='")
        field, value = piece.split("=", 1)
        parsed[field] = int(value) if field == "ws" else value
    return parsed


def naive_key(resource_id: str) -> str:
    return resource_id


def key_collides(left: str, right: str) -> bool:
    return left == right
