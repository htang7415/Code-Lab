from activations_softmax_softplus_softsign import softmax, softplus, softsign


def test_softmax_sum():
    row = softmax([1.0, 1.0])
    assert abs(sum(row) - 1.0) < 1e-6
    assert softplus(0.0) > 0.0
    assert abs(softsign(1.0) - 0.5) < 1e-6
