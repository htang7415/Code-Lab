from lr_step_decay import step_decay


def test_step_decay():
    assert step_decay(0.1, 10, 0.5, 10) == 0.05
