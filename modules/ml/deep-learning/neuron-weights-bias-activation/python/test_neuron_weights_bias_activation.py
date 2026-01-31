from neuron_weights_bias_activation import neuron


def test_neuron_output_range():
    out = neuron([1.0, 1.0], [1.0, 1.0], 0.0)
    assert 0.0 < out < 1.0
