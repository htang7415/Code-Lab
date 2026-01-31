from empirical_pmf import empirical_pmf


def test_empirical_pmf():
    pmf = empirical_pmf([1, 1, 2])
    assert pmf[1] == 2 / 3
