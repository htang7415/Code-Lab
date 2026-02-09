from automatic_differentiation import Value


def test_value_mul_add_relu_backward():
    a = Value(2.0)
    b = Value(-3.0)
    c = Value(10.0)
    out = (a * b + c).relu()
    out.backward()

    assert out.data == 4.0
    assert a.grad == -3.0
    assert b.grad == 2.0
    assert c.grad == 1.0


def test_value_zero_grad_single_node():
    x = Value(3.0)
    y = x * 2.0
    y.backward()
    assert x.grad == 2.0
    x.zero_grad()
    assert x.grad == 0.0
