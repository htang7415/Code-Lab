from weight_decay import weight_decay_step


def test_weight_decay_step():
    assert weight_decay_step(1.0, 0.0, 0.1, 0.1) == 0.99
