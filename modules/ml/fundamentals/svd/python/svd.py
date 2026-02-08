import math


def svd_2x2(a: list[list[float]]) -> tuple[list[list[float]], list[float], list[list[float]]]:
    """
    Compute SVD of a 2x2 matrix using one Jacobi rotation on B = A^T A.
    Returns (U, S, Vt) such that A ≈ U @ diag(S) @ Vt.
    """
    a00, a01 = a[0]
    a10, a11 = a[1]

    # B = A^T A (symmetric 2x2)
    b00 = a00 * a00 + a10 * a10
    b01 = a00 * a01 + a10 * a11
    b11 = a01 * a01 + a11 * a11

    eps = 1e-12

    # Jacobi rotation to diagonalize B
    if abs(b01) <= eps:
        c, s = 1.0, 0.0
    else:
        tau = (b11 - b00) / (2.0 * b01)
        if tau == 0.0:
            t = 1.0
        else:
            t = math.copysign(1.0, tau) / (abs(tau) + math.sqrt(1.0 + tau * tau))
        c = 1.0 / math.sqrt(1.0 + t * t)
        s = t * c

    v00, v01 = c, -s
    v10, v11 = s, c

    # Eigenvalues (diagonal entries of V^T B V)
    cs = c * s
    c2 = c * c
    s2 = s * s
    lam1 = c2 * b00 - 2.0 * cs * b01 + s2 * b11
    lam2 = s2 * b00 + 2.0 * cs * b01 + c2 * b11

    if lam1 < 0.0:
        lam1 = 0.0
    if lam2 < 0.0:
        lam2 = 0.0

    s1 = math.sqrt(lam1)
    s2v = math.sqrt(lam2)

    # Sort singular values descending; swap V columns if needed.
    if s2v > s1:
        s1, s2v = s2v, s1
        v00, v01 = v01, v00
        v10, v11 = v11, v10

    v = [[v00, v01], [v10, v11]]
    vt = [[v00, v10], [v01, v11]]
    svals = [s1, s2v]

    if svals[0] <= eps:
        return [[1.0, 0.0], [0.0, 1.0]], [0.0, 0.0], [[1.0, 0.0], [0.0, 1.0]]

    # U = A V Σ^{-1}
    av00 = a00 * v00 + a01 * v10
    av10 = a10 * v00 + a11 * v10
    av01 = a00 * v01 + a01 * v11
    av11 = a10 * v01 + a11 * v11

    u00 = av00 / svals[0]
    u10 = av10 / svals[0]

    if svals[1] > eps:
        u01 = av01 / svals[1]
        u11 = av11 / svals[1]
    else:
        # Any unit vector orthogonal to U[:,0]
        u01 = -u10
        u11 = u00

    u = [[u00, u01], [u10, u11]]
    return u, svals, vt


def singular_values_2x2(a: list[list[float]]) -> list[float]:
    _, svals, _ = svd_2x2(a)
    return svals
