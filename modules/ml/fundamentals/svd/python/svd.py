import math


def singular_values_2x2(a: list[list[float]]) -> list[float]:
    # compute eigenvalues of A^T A
    at_a = [
        [a[0][0] ** 2 + a[1][0] ** 2, a[0][0] * a[0][1] + a[1][0] * a[1][1]],
        [a[0][0] * a[0][1] + a[1][0] * a[1][1], a[0][1] ** 2 + a[1][1] ** 2],
    ]
    trace = at_a[0][0] + at_a[1][1]
    det = at_a[0][0] * at_a[1][1] - at_a[0][1] * at_a[1][0]
    eig1 = trace / 2 + math.sqrt(max(0.0, (trace / 2) ** 2 - det))
    eig2 = trace / 2 - math.sqrt(max(0.0, (trace / 2) ** 2 - det))
    return [math.sqrt(eig1), math.sqrt(eig2)]
