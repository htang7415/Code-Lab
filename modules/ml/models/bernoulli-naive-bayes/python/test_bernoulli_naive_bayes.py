from bernoulli_naive_bayes import bernoulli_log_likelihood


def test_bernoulli_log_likelihood():
    ll = bernoulli_log_likelihood([1, 0], [0.8, 0.2])
    assert ll > -1.0
