from vae_posterior_collapse import kl_is_low


def test_kl_is_low():
    assert kl_is_low(0.05)
