def longest_prefix_cache_hit(
    prompt_tokens: list[int],
    cached_prefixes: list[list[int]],
) -> int:
    best = 0
    for cached in cached_prefixes:
        length = 0
        for token, cached_token in zip(prompt_tokens, cached):
            if token != cached_token:
                break
            length += 1
        best = max(best, length)
    return best
