from __future__ import annotations


def bucketize(values: list[float], boundaries: list[float]) -> list[int]:
    if any(boundaries[index] > boundaries[index + 1] for index in range(len(boundaries) - 1)):
        raise ValueError("boundaries must be sorted in nondecreasing order")

    bucket_indices: list[int] = []
    for value in values:
        bucket = len(boundaries)
        for index, boundary in enumerate(boundaries):
            if value < boundary:
                bucket = index
                break
        bucket_indices.append(bucket)
    return bucket_indices


def category_cross_features(left: list[str], right: list[str], separator: str = "__X__") -> list[str]:
    if len(left) != len(right):
        raise ValueError("left and right must have the same length")

    return [f"{left_value}{separator}{right_value}" for left_value, right_value in zip(left, right)]


def pooled_entity_embedding(entity_ids: list[int], embedding_table: list[list[float]]) -> list[float]:
    if not embedding_table:
        raise ValueError("embedding_table must be non-empty")

    embedding_dim = len(embedding_table[0])
    if any(len(row) != embedding_dim for row in embedding_table):
        raise ValueError("all embedding rows must have the same length")

    if not entity_ids:
        return [0.0] * embedding_dim
    if any(entity_id < 0 or entity_id >= len(embedding_table) for entity_id in entity_ids):
        raise ValueError("entity_ids must index valid embedding rows")

    pooled = [0.0] * embedding_dim
    for entity_id in entity_ids:
        row = embedding_table[entity_id]
        for index, value in enumerate(row):
            pooled[index] += value
    return [value / len(entity_ids) for value in pooled]
