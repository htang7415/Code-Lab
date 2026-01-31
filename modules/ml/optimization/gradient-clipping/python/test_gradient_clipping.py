from gradient_clipping import clip_norm


def test_clip_norm():
    grad = clip_norm([3.0, 4.0], clip=5.0)
    assert grad == [3.0, 4.0]
    grad2 = clip_norm([3.0, 4.0], clip=2.5)
    assert sum(g * g for g in grad2) <= 6.25 + 1e-6
