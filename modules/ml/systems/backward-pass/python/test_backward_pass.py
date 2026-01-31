from backward_pass import backward


def test_backward():
    assert backward(2.0, 3.0) == 6.0
