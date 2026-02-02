from problem_376_wiggle_subsequence import Solution


def test_wiggle_basic():
    assert Solution().wiggleMaxLength([1, 7, 4, 9, 2, 5]) == 6


def test_wiggle_flat():
    assert Solution().wiggleMaxLength([1, 1, 1, 1]) == 1
