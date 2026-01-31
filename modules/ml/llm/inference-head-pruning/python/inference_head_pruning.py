from __future__ import annotations


def prune_heads(weights: list[list[float]], keep: list[int], head_dim: int) -> list[list[float]]:
    pruned = []
    for row in weights:
        new_row = []
        for h in keep:
            start = h * head_dim
            end = start + head_dim
            new_row.extend(row[start:end])
        pruned.append(new_row)
    return pruned
