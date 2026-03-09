from __future__ import annotations


def prefix_cache_savings(
    prompt_lengths: list[int],
    hit_lengths: list[int],
) -> tuple[int, float]:
    if len(prompt_lengths) != len(hit_lengths):
        raise ValueError("prompt_lengths and hit_lengths must have the same length")
    if any(length <= 0 for length in prompt_lengths):
        raise ValueError("prompt_lengths must be positive")

    saved_tokens = 0
    total_tokens = sum(prompt_lengths)
    for prompt_length, hit_length in zip(prompt_lengths, hit_lengths):
        if hit_length < 0:
            raise ValueError("hit_lengths must be non-negative")
        if hit_length > prompt_length:
            raise ValueError("hit_length cannot exceed prompt_length")
        saved_tokens += hit_length

    return saved_tokens, saved_tokens / total_tokens
