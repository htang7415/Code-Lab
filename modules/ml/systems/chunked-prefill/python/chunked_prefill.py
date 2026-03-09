from __future__ import annotations


def chunked_prefill_rounds(prompt_lengths: list[int], chunk_size: int) -> list[int]:
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")
    if any(length <= 0 for length in prompt_lengths):
        raise ValueError("prompt_lengths must be positive")
    if not prompt_lengths:
        return []

    remaining = prompt_lengths[:]
    rounds: list[int] = []

    while any(length > 0 for length in remaining):
        round_tokens = sum(min(length, chunk_size) for length in remaining)
        rounds.append(round_tokens)
        remaining = [max(length - chunk_size, 0) for length in remaining]

    return rounds
