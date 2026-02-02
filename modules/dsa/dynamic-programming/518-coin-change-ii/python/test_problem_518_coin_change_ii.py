from problem_518_coin_change_ii import Solution


def test_coin_change_ii_basic():
    assert Solution().change(5, [1, 2, 5]) == 4


def test_coin_change_ii_none():
    assert Solution().change(3, [2]) == 0
