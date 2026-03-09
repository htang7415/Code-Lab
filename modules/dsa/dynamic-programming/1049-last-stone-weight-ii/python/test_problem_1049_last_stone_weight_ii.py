from problem_1049_last_stone_weight_ii import Solution


def test_last_stone_example():
    assert Solution().lastStoneWeightII([2, 7, 4, 1, 8, 1]) == 1


def test_last_stone_edge_single():
    assert Solution().lastStoneWeightII([5]) == 5


def test_last_stone_tricky_balanced_partition():
    assert Solution().lastStoneWeightII([1, 1, 4, 2, 2]) == 0
