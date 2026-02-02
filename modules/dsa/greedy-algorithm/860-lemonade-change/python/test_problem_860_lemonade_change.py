from problem_860_lemonade_change import Solution


def test_lemonade_change_true():
    assert Solution().lemonadeChange([5, 5, 5, 10, 20]) is True


def test_lemonade_change_false():
    assert Solution().lemonadeChange([5, 5, 10, 10, 20]) is False
