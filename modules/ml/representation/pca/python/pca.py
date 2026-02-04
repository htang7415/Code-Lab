import math


def first_principal_component_2d(points: list[list[float]]) -> list[float]:
    if not points:
        return [0.0, 0.0]

    mean_x = sum(p[0] for p in points) / len(points)
    mean_y = sum(p[1] for p in points) / len(points)

    cov_xx = 0.0
    cov_xy = 0.0
    cov_yy = 0.0
    for x, y in points:
        dx = x - mean_x
        dy = y - mean_y
        cov_xx += dx * dx
        cov_xy += dx * dy
        cov_yy += dy * dy
    cov_xx /= len(points)
    cov_xy /= len(points)
    cov_yy /= len(points)

    trace = cov_xx + cov_yy
    det = cov_xx * cov_yy - cov_xy * cov_xy
    disc = max(trace * trace - 4 * det, 0.0)
    lambda_max = (trace + math.sqrt(disc)) / 2

    if abs(cov_xy) > 1e-12:
        vx = cov_xy
        vy = lambda_max - cov_xx
    else:
        if cov_xx >= cov_yy:
            vx, vy = 1.0, 0.0
        else:
            vx, vy = 0.0, 1.0

    norm = math.hypot(vx, vy)
    if norm == 0:
        return [0.0, 0.0]
    return [vx / norm, vy / norm]
