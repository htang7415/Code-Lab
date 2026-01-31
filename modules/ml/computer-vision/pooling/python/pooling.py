def max_pool(window: list[float]) -> float:
    return max(window)


def avg_pool(window: list[float]) -> float:
    return sum(window) / len(window)
