from problem_213_house_robber_ii import Solution


def test_house_robber_ii_basic():
    assert Solution().rob([2, 3, 2]) == 3


def test_house_robber_ii_more():
    assert Solution().rob([1, 2, 3, 1]) == 4
