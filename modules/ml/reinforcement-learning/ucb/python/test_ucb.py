from ucb import ucb_score


def test_ucb_score():
    assert ucb_score(0.5, 10, 2, 1.0) > 0.5
