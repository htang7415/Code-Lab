from convolution_layer import conv2d


def test_conv2d_shape():
    image = [[1, 2], [3, 4]]
    kernel = [[1]]
    assert conv2d(image, kernel) == [[1, 2], [3, 4]]
