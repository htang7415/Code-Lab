from feedforward_neural_network import feedforward


def test_feedforward_shape():
    x = [1.0, -1.0]
    w1 = [[1.0, 0.0], [0.0, 1.0]]
    b1 = [0.0, 0.0]
    out = feedforward(x, [w1], [b1])
    assert len(out) == 2
