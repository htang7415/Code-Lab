def calinski_harabasz(b: float, w: float, k: int, n: int) -> float:
    return (b / (k - 1)) / (w / (n - k))
