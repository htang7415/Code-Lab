from multiple_knapsack_theory import Solution


def test_multiple_knapsack_basic():
    assert Solution().multipleKnapsack([1, 3], [15, 20], [2, 1], 4) == 35
