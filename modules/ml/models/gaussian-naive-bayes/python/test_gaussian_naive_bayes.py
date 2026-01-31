from gaussian_naive_bayes import gaussian_log_likelihood


def test_gaussian_log_likelihood():
    ll = gaussian_log_likelihood([0.0], [0.0], [1.0])
    assert ll < 0.0
