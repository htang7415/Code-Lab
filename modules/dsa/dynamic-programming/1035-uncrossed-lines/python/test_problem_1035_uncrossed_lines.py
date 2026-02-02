from problem_1035_uncrossed_lines import Solution


def test_uncrossed_lines_basic():
    assert Solution().maxUncrossedLines([1, 4, 2], [1, 2, 4]) == 2


def test_uncrossed_lines_more():
    assert Solution().maxUncrossedLines([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]) == 3
