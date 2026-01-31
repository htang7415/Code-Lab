def bilinear_sample(v00: float, v01: float, v10: float, v11: float, tx: float, ty: float) -> float:
    a = v00 * (1 - tx) + v10 * tx
    b = v01 * (1 - tx) + v11 * tx
    return a * (1 - ty) + b * ty
