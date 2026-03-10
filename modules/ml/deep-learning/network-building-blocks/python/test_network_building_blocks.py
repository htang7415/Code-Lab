from __future__ import annotations

from network_building_blocks import feedforward, neuron


def test_neuron_output_range() -> None:
    out = neuron([1.0, 1.0], [1.0, 1.0], 0.0)
    assert 0.0 < out < 1.0


def test_feedforward_shape() -> None:
    x = [1.0, -1.0]
    w1 = [[1.0, 0.0], [0.0, 1.0]]
    b1 = [0.0, 0.0]
    out = feedforward(x, [w1], [b1])
    assert len(out) == 2
