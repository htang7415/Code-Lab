from problem_121_best_time_to_buy_and_sell_stock import Solution


def test_stock_example():
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 5


def test_stock_edge_single_day():
    assert Solution().maxProfit([5]) == 0


def test_stock_tricky_late_minimum():
    assert Solution().maxProfit([2, 4, 1]) == 2
