from problem_115_distinct_subsequences import Solution


def test_distinct_subsequences_example():
    assert Solution().numDistinct("rabbbit", "rabbit") == 3


def test_distinct_subsequences_edge_empty_target():
    assert Solution().numDistinct("abc", "") == 1


def test_distinct_subsequences_tricky_repeated_choices():
    assert Solution().numDistinct("babgbag", "bag") == 5
