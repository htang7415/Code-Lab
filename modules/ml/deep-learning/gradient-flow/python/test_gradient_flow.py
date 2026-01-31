from gradient_flow import propagate_variance


def test_propagate_variance():
    assert propagate_variance(1.0, [0.5, 2.0]) == 1.0
