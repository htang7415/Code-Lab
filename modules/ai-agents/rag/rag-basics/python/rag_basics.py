from __future__ import annotations


def select_top_k(scored_chunks: list[tuple[str, float]], k: int) -> list[str]:
    if k <= 0:
        raise ValueError("k must be positive")
    ranked = sorted(scored_chunks, key=lambda item: item[1], reverse=True)
    return [chunk for chunk, _score in ranked[:k]]


def build_grounded_context(chunks: list[str], max_chunks: int) -> str:
    if max_chunks <= 0:
        raise ValueError("max_chunks must be positive")
    selected = [chunk.strip() for chunk in chunks[:max_chunks] if chunk.strip()]
    return "\n\n".join(f"[{i + 1}] {chunk}" for i, chunk in enumerate(selected))
