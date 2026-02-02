from problem_216_combination_sum_iii import Solution


def test_combination_sum_iii_basic():
    result = Solution().combinationSum3(3, 7)
    assert result == [[1, 2, 4]]


def test_combination_sum_iii_multiple():
    result = Solution().combinationSum3(3, 9)
    assert sorted(result) == [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
