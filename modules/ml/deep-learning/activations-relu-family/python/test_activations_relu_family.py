from activations_relu_family import relu_family


def test_relu_family():
    out = relu_family(-2.0, alpha=0.1)
    assert out["relu"] == 0.0
    assert out["leaky_relu"] < 0.0
