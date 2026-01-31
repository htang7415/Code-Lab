from beta_binomial import beta_posterior


def test_beta_posterior():
    assert beta_posterior(1.0, 1.0, 3, 2) == (4.0, 3.0)
