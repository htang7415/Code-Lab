from problem_121_best_time_to_buy_and_sell_stock import Solution


def test_stock_basic():
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 5


def test_stock_none():
    assert Solution().maxProfit([7, 6, 4, 3, 1]) == 0
