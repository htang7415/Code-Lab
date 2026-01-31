from backpropagation import linear_backprop


def test_linear_backprop():
    grad_w = linear_backprop(3.0, 2.0, 0.5)
    assert grad_w == 1.5
