import pytest

from convolution_layer import conv2d


def test_conv2d_computes_valid_convolution():
    image = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    kernel = [
        [1, 0],
        [0, -1],
    ]
    assert conv2d(image, kernel) == [[-4.0, -4.0], [-4.0, -4.0]]


def test_conv2d_rejects_oversized_kernel():
    with pytest.raises(ValueError, match="fit inside"):
        conv2d([[1.0]], [[1.0, 0.0]])
