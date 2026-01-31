from activations_sigmoid_tanh import activations, dynamic_tanh


def test_activations_range():
    out = activations(2.0)
    assert 0.0 <= out["sigmoid"] <= 1.0
    assert -1.0 <= out["tanh"] <= 1.0


def test_dynamic_tanh_parameters():
    assert dynamic_tanh(0.0, alpha=2.0, gamma=3.0, beta=0.5) == 0.5
