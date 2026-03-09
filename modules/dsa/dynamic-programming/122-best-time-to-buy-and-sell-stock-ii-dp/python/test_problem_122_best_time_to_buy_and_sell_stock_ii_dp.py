from problem_122_best_time_to_buy_and_sell_stock_ii_dp import Solution


def test_stock_ii_example():
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 7


def test_stock_ii_edge_empty():
    assert Solution().maxProfit([]) == 0


def test_stock_ii_tricky_all_rising():
    assert Solution().maxProfit([1, 2, 3, 4, 5]) == 4
