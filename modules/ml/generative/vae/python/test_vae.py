from vae import elbo


def test_elbo():
    assert elbo(2.0, 0.5) == 1.5
