from diffusion_models import add_noise


def test_add_noise():
    assert abs(add_noise(1.0, 0.0, 1.0) - 1.0) < 1e-6
