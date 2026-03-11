def max_pool(window: list[float]) -> float:
    if not window:
        raise ValueError("window must be non-empty")
    return max(window)


def avg_pool(window: list[float]) -> float:
    if not window:
        raise ValueError("window must be non-empty")
    return sum(window) / len(window)
