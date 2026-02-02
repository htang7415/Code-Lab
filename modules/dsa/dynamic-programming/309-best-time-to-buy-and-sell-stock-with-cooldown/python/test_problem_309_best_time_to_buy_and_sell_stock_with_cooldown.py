from problem_309_best_time_to_buy_and_sell_stock_with_cooldown import Solution


def test_stock_cooldown_basic():
    assert Solution().maxProfit([1, 2, 3, 0, 2]) == 3


def test_stock_cooldown_single():
    assert Solution().maxProfit([1]) == 0
