from kl_divergence import kl


def test_kl():
    assert abs(kl([0.5, 0.5], [0.5, 0.5])) < 1e-6
