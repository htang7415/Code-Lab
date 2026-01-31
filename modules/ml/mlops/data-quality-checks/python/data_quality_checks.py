from typing import Optional


def missing_rate(values: list[Optional[float]]) -> float:
    missing = sum(1 for v in values if v is None)
    return missing / len(values)
