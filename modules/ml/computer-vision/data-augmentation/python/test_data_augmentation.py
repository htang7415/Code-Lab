from data_augmentation import horizontal_flip


def test_horizontal_flip():
    assert horizontal_flip([[1, 2]]) == [[2, 1]]
