from problem_188_best_time_to_buy_and_sell_stock_iv import Solution


def test_stock_iv_basic():
    assert Solution().maxProfit(2, [2, 4, 1]) == 2


def test_stock_iv_more():
    assert Solution().maxProfit(2, [3, 2, 6, 5, 0, 3]) == 7
