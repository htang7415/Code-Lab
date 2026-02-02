from problem_746_min_cost_climbing_stairs import Solution


def test_min_cost_basic():
    assert Solution().minCostClimbingStairs([10, 15, 20]) == 15


def test_min_cost_more():
    assert Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
