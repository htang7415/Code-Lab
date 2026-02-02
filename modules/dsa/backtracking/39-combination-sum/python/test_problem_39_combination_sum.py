from problem_39_combination_sum import Solution


def test_combination_sum_basic():
    result = Solution().combinationSum([2, 3, 6, 7], 7)
    assert sorted(sorted(combo) for combo in result) == [[2, 2, 3], [7]]


def test_combination_sum_single():
    result = Solution().combinationSum([2], 1)
    assert result == []
