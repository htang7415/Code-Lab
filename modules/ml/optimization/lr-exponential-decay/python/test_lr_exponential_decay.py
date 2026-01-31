from lr_exponential_decay import exp_decay


def test_exp_decay():
    assert exp_decay(0.1, 0.0, 10) == 0.1
