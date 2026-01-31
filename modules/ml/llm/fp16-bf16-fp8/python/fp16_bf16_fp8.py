import math


def quantize_fp(x: float, mantissa_bits: int) -> float:
    if x == 0.0:
        return 0.0
    exp = int(math.floor(math.log2(abs(x))))
    scale = 2 ** (mantissa_bits - exp)
    return round(x * scale) / scale
