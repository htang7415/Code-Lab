from image_preprocessing import normalize_pixels


def test_normalize_pixels():
    assert normalize_pixels([0, 255]) == [0.0, 1.0]
