from positional_encoding import sinusoidal_position


def test_positional_encoding_shape():
    vec = sinusoidal_position(3, 6)
    assert len(vec) == 6
    assert vec[0] != vec[1]
