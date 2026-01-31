from sparse_attention import window_mask


def test_window_mask():
    mask = window_mask(4, 1)
    assert mask[0] == [1, 1, 0, 0]
