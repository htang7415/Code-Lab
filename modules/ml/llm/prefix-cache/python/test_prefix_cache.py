from prefix_cache import longest_prefix_cache_hit


def test_longest_prefix_cache_hit_uses_longest_matching_prefix():
    prompt = [101, 11, 12, 13]
    cached = [
        [101, 11],
        [101, 11, 12],
        [99, 1, 2],
    ]
    assert longest_prefix_cache_hit(prompt, cached) == 3


def test_longest_prefix_cache_hit_zero_when_no_prefix_matches():
    assert longest_prefix_cache_hit([1, 2], [[3, 4], [5]]) == 0
