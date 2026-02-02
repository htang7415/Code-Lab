from problem_494_target_sum import Solution


def test_target_sum_basic():
    assert Solution().findTargetSumWays([1, 1, 1, 1, 1], 3) == 5


def test_target_sum_single():
    assert Solution().findTargetSumWays([1], 1) == 1
