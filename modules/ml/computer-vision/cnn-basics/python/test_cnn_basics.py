from cnn_basics import conv1d


def test_conv1d():
    assert conv1d([1, 2, 3], [1, 0]) == [1, 2]
