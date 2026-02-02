from problem_300_longest_increasing_subsequence import Solution


def test_lis_basic():
    assert Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4


def test_lis_more():
    assert Solution().lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4
