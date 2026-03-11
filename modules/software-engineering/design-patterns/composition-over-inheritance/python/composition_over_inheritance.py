from __future__ import annotations

from collections.abc import Callable


Transform = Callable[[str], str]


def normalize_label(value: str) -> str:
    return " ".join(value.strip().split())


def badge(label: str) -> Transform:
    def apply(value: str) -> str:
        return f"{value} [{label}]"

    return apply


def compose_label(value: str, transforms: list[Transform]) -> str:
    result = value
    for transform in transforms:
        result = transform(result)
    return result
