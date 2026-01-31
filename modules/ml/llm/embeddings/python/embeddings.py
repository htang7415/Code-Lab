from __future__ import annotations


def embed(tokens: list[int], embeddings: list[list[float]]) -> list[list[float]]:
    return [embeddings[i] for i in tokens]
