from sgd import sgd_step


def test_sgd_step():
    assert sgd_step(1.0, 0.5, 0.1) == 0.95
