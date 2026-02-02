from problem_377_combination_sum_iv import Solution


def test_combination_sum_iv_basic():
    assert Solution().combinationSum4([1, 2, 3], 4) == 7


def test_combination_sum_iv_none():
    assert Solution().combinationSum4([9], 3) == 0
