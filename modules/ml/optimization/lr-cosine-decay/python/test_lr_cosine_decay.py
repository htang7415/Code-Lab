from lr_cosine_decay import cosine_decay


def test_cosine_decay_end():
    assert abs(cosine_decay(1.0, 10, 10)) < 1e-6
