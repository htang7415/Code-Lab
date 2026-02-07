import math


def pca_first_component_2d(points: list[list[float]]) -> list[float]:
    n = len(points)
    mean_x = sum(p[0] for p in points) / n
    mean_y = sum(p[1] for p in points) / n
    cov_xx = sum((p[0] - mean_x) ** 2 for p in points) / n
    cov_yy = sum((p[1] - mean_y) ** 2 for p in points) / n
    cov_xy = sum((p[0] - mean_x) * (p[1] - mean_y) for p in points) / n
    # eigenvector for largest eigenvalue of 2x2
    trace = cov_xx + cov_yy
    det = cov_xx * cov_yy - cov_xy * cov_xy
    eig1 = trace / 2 + math.sqrt(max(0.0, (trace / 2) ** 2 - det))
    if cov_xy == 0:
        vec = [1.0, 0.0] if cov_xx >= cov_yy else [0.0, 1.0]
    else:
        vec = [eig1 - cov_yy, cov_xy]
    norm = math.sqrt(vec[0] ** 2 + vec[1] ** 2)
    return [vec[0] / norm, vec[1] / norm]
