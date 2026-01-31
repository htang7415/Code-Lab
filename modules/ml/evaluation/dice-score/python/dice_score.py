def dice(a: set[int], b: set[int]) -> float:
    inter = len(a & b)
    return 2 * inter / (len(a) + len(b)) if (len(a) + len(b)) > 0 else 0.0
