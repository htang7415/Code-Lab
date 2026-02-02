from problem_135_candy import Solution


def test_candy_basic():
    assert Solution().candy([1, 0, 2]) == 5


def test_candy_equal():
    assert Solution().candy([1, 2, 2]) == 4
