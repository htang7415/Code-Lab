from __future__ import annotations


def _solve_linear_system(matrix: list[list[float]], rhs: list[float]) -> list[float]:
    n = len(matrix)
    augmented = [row[:] + [rhs_value] for row, rhs_value in zip(matrix, rhs)]

    for pivot in range(n):
        pivot_row = max(range(pivot, n), key=lambda row: abs(augmented[row][pivot]))
        if abs(augmented[pivot_row][pivot]) < 1e-12:
            raise ValueError("matrix is singular")
        augmented[pivot], augmented[pivot_row] = augmented[pivot_row], augmented[pivot]

        pivot_value = augmented[pivot][pivot]
        for column in range(pivot, n + 1):
            augmented[pivot][column] /= pivot_value

        for row in range(n):
            if row == pivot:
                continue
            factor = augmented[row][pivot]
            for column in range(pivot, n + 1):
                augmented[row][column] -= factor * augmented[pivot][column]

    return [augmented[row][-1] for row in range(n)]


def lle_weights(
    point: list[float],
    neighbors: list[list[float]],
    regularization: float = 1e-3,
) -> list[float]:
    if regularization < 0.0:
        raise ValueError("regularization must be non-negative")
    if not neighbors:
        raise ValueError("neighbors must not be empty")
    if any(len(neighbor) != len(point) for neighbor in neighbors):
        raise ValueError("neighbors must match the point dimension")
    if len(neighbors) == 1:
        return [1.0]

    diffs = [[point[d] - neighbor[d] for d in range(len(point))] for neighbor in neighbors]
    covariance = []
    for diff_i in diffs:
        covariance.append([
            sum(a * b for a, b in zip(diff_i, diff_j)) for diff_j in diffs
        ])

    trace = sum(covariance[i][i] for i in range(len(covariance)))
    ridge = regularization * trace if trace > 0.0 else regularization
    for i in range(len(covariance)):
        covariance[i][i] += ridge

    raw_weights = _solve_linear_system(covariance, [1.0] * len(neighbors))
    total = sum(raw_weights)
    return [weight / total for weight in raw_weights]
