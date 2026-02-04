import math

from positional_encoding import sinusoidal_position_encoding


def test_sinusoidal_position_encoding_shape():
    table = sinusoidal_position_encoding(3, 4)
    assert len(table) == 3
    assert all(len(row) == 4 for row in table)


def test_sinusoidal_position_encoding_values():
    table = sinusoidal_position_encoding(2, 4)
    assert table[0] == [0.0, 1.0, 0.0, 1.0]
    assert math.isclose(table[1][0], math.sin(1.0), rel_tol=1e-6)
    assert math.isclose(table[1][1], math.cos(1.0), rel_tol=1e-6)
    assert math.isclose(table[1][2], math.sin(1.0 / 100), rel_tol=1e-6)
    assert math.isclose(table[1][3], math.cos(1.0 / 100), rel_tol=1e-6)
