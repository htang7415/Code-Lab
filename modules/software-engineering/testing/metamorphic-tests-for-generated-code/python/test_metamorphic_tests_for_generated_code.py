from __future__ import annotations

import pytest

from metamorphic_tests_for_generated_code import (
    metamorphic_failures,
    preserves_idempotence,
    sorted_unique,
)


def test_sorted_unique_normalizes_case_order_and_duplicates() -> None:
    assert sorted_unique(["B", "a", "a", " "]) == ["a", "b"]


def test_metamorphic_failures_detects_invariant_violations() -> None:
    assert metamorphic_failures(
        sorted_unique,
        [["b", "a", "a"], ["a", "b"], ["A", "b", ""]],
    ) == []

    assert metamorphic_failures(
        lambda values: values,
        [["b", "a"], ["a", "b"]],
    ) == [1]


def test_preserves_idempotence_checks_repeat_application() -> None:
    assert preserves_idempotence(["A", "a", "b"]) is True

    with pytest.raises(ValueError):
        metamorphic_failures(sorted_unique, [])
