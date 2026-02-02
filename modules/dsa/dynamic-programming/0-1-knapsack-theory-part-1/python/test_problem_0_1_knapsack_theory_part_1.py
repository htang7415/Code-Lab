from problem_0_1_knapsack_theory_part_1 import Solution


def test_knapsack_part1_basic():
    assert Solution().knapSack([1, 3, 4], [15, 20, 30], 4) == 35
