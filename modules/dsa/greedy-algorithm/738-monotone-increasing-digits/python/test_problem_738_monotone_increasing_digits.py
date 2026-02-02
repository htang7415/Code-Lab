from problem_738_monotone_increasing_digits import Solution


def test_monotone_digits_basic():
    assert Solution().monotoneIncreasingDigits(10) == 9


def test_monotone_digits_more():
    assert Solution().monotoneIncreasingDigits(332) == 299
