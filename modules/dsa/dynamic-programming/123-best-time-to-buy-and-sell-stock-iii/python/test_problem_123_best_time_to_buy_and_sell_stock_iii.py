from problem_123_best_time_to_buy_and_sell_stock_iii import Solution


def test_stock_iii_basic():
    assert Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4]) == 6


def test_stock_iii_more():
    assert Solution().maxProfit([1, 2, 3, 4, 5]) == 4
