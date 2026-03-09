from problem_123_best_time_to_buy_and_sell_stock_iii import Solution


def test_stock_iii_example():
    assert Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4]) == 6


def test_stock_iii_edge_single_day():
    assert Solution().maxProfit([1]) == 0


def test_stock_iii_tricky_two_transactions():
    assert Solution().maxProfit([1, 2, 4, 2, 5, 7, 2, 4, 9, 0]) == 13
