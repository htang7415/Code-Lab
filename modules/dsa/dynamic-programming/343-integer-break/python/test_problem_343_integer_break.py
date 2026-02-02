from problem_343_integer_break import Solution


def test_integer_break_small():
    assert Solution().integerBreak(2) == 1


def test_integer_break_large():
    assert Solution().integerBreak(10) == 36
