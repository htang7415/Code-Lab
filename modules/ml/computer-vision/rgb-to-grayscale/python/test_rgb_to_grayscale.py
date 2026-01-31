from rgb_to_grayscale import rgb_to_gray


def test_rgb_to_gray():
    assert round(rgb_to_gray(255, 255, 255)) == 255
