def mean_shift(old: list[float], new: list[float]) -> float:
    mean_old = sum(old) / len(old)
    mean_new = sum(new) / len(new)
    return abs(mean_new - mean_old)
