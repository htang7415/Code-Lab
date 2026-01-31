from diffusion_guidance_tradeoffs import guided_step


def test_guided_step():
    assert guided_step(0.0, 1.0, 0.5) == 0.5
