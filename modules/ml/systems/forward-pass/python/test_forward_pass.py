from forward_pass import forward


def test_forward():
    assert forward([1.0, 2.0], [1.0, 1.0], 0.0) == 3.0
