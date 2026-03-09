from __future__ import annotations


def category_cross_features(left: list[str], right: list[str], separator: str = "__X__") -> list[str]:
    if len(left) != len(right):
        raise ValueError("left and right must have the same length")

    return [f"{left_value}{separator}{right_value}" for left_value, right_value in zip(left, right)]
