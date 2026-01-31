from check_gradients import gradients_ok


def test_gradients_ok():
    assert gradients_ok([0.0, 1.0])
    assert not gradients_ok([0.0, 0.0])
