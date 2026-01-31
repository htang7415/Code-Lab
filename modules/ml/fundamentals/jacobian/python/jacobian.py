def jacobian(f1, f2, x: float, y: float, eps: float = 1e-5) -> list[list[float]]:
    df1_dx = (f1(x + eps, y) - f1(x - eps, y)) / (2 * eps)
    df1_dy = (f1(x, y + eps) - f1(x, y - eps)) / (2 * eps)
    df2_dx = (f2(x + eps, y) - f2(x - eps, y)) / (2 * eps)
    df2_dy = (f2(x, y + eps) - f2(x, y - eps)) / (2 * eps)
    return [[df1_dx, df1_dy], [df2_dx, df2_dy]]
