import math


def sinusoidal_position_encoding(length: int, dim: int) -> list[list[float]]:
    if length <= 0 or dim <= 0:
        return []
    table: list[list[float]] = []
    for pos in range(length):
        row: list[float] = [0.0] * dim
        for i in range(dim):
            pair_index = i // 2
            denom = 10000 ** (2 * pair_index / dim)
            angle = pos / denom
            row[i] = math.sin(angle) if i % 2 == 0 else math.cos(angle)
        table.append(row)
    return table
