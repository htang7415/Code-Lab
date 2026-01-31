def quantize_int(x: float, bits: int, scale: float) -> int:
    qmax = 2 ** (bits - 1) - 1
    q = int(round(x / scale))
    return max(-qmax, min(qmax, q))
