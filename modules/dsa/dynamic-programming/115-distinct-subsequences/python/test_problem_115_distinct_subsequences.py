from problem_115_distinct_subsequences import Solution


def test_distinct_subsequences_basic():
    assert Solution().numDistinct("rabbbit", "rabbit") == 3


def test_distinct_subsequences_more():
    assert Solution().numDistinct("babgbag", "bag") == 5
