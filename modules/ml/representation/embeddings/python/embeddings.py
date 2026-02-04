def mean_pool(embeddings: list[list[float]]) -> list[float]:
    if not embeddings:
        return []
    dim = len(embeddings[0])
    totals = [0.0] * dim
    for vector in embeddings:
        for i in range(dim):
            totals[i] += vector[i]
    return [value / len(embeddings) for value in totals]
