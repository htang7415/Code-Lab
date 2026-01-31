def batch_stats(matrix: list[list[float]]) -> tuple[float, float]:
    values = [v for row in matrix for v in row]
    mean = sum(values) / len(values)
    var = sum((v - mean) ** 2 for v in values) / len(values)
    return mean, var
