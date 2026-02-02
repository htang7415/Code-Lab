from problem_1049_last_stone_weight_ii import Solution


def test_last_stone_basic():
    assert Solution().lastStoneWeightII([2, 7, 4, 1, 8, 1]) == 1


def test_last_stone_more():
    assert Solution().lastStoneWeightII([31, 26, 33, 21, 40]) == 5
