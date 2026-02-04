from autoencoder import linear_autoencode


def test_linear_autoencoder_identity():
    W = [[1.0, 0.0], [0.0, 1.0]]
    x = [2.0, -1.0]
    assert linear_autoencode(x, W) == x


def test_linear_autoencoder_projection():
    W = [[1.0, 0.0]]
    x = [3.0, 4.0]
    assert linear_autoencode(x, W) == [3.0, 0.0]
