from problem_198_house_robber import Solution


def test_house_robber_basic():
    assert Solution().rob([1, 2, 3, 1]) == 4


def test_house_robber_more():
    assert Solution().rob([2, 7, 9, 3, 1]) == 12
