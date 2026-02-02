from complete_knapsack_theory import Solution


def test_complete_knapsack_basic():
    assert Solution().completeKnapsack([1, 3, 4], [15, 20, 30], 4) == 60
