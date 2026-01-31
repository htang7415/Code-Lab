import math


def has_nan(values: list[float]) -> bool:
    return any(math.isnan(v) for v in values)
