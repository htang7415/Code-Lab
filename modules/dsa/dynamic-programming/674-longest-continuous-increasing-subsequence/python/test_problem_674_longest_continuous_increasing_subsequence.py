from problem_674_longest_continuous_increasing_subsequence import Solution


def test_lcis_basic():
    assert Solution().findLengthOfLCIS([1, 3, 5, 4, 7]) == 3


def test_lcis_flat():
    assert Solution().findLengthOfLCIS([2, 2, 2, 2]) == 1
