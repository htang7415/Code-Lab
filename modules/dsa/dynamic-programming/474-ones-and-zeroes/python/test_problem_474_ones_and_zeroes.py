from problem_474_ones_and_zeroes import Solution


def test_ones_and_zeroes_basic():
    assert Solution().findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3) == 4


def test_ones_and_zeroes_small():
    assert Solution().findMaxForm(["10", "0", "1"], 1, 1) == 2
