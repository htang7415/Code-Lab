from problem_122_best_time_to_buy_and_sell_stock_ii_dp import Solution


def test_stock_ii_basic():
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 7


def test_stock_ii_none():
    assert Solution().maxProfit([7, 6, 4, 3, 1]) == 0
