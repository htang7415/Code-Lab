from __future__ import annotations

from collections.abc import Callable


def sorted_unique(values: list[str]) -> list[str]:
    return sorted({value.strip().lower() for value in values if value.strip()})


def metamorphic_failures(
    evaluator: Callable[[list[str]], list[str]],
    equivalent_inputs: list[list[str]],
) -> list[int]:
    if not equivalent_inputs:
        raise ValueError("equivalent_inputs must be non-empty")

    expected = evaluator(equivalent_inputs[0])
    return [
        index
        for index, values in enumerate(equivalent_inputs[1:], start=1)
        if evaluator(values) != expected
    ]


def preserves_idempotence(values: list[str]) -> bool:
    return sorted_unique(sorted_unique(values)) == sorted_unique(values)
