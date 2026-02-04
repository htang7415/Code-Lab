import math


def singular_values_2x2(matrix: list[list[float]]) -> list[float]:
    a, b = matrix[0]
    c, d = matrix[1]

    s11 = a * a + c * c
    s12 = a * b + c * d
    s22 = b * b + d * d

    trace = s11 + s22
    det = s11 * s22 - s12 * s12
    disc = max(trace * trace - 4 * det, 0.0)
    lambda1 = (trace + math.sqrt(disc)) / 2
    lambda2 = (trace - math.sqrt(disc)) / 2

    sigma1 = math.sqrt(max(lambda1, 0.0))
    sigma2 = math.sqrt(max(lambda2, 0.0))
    return sorted([sigma1, sigma2], reverse=True)
