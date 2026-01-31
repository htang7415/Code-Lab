from data_leakage import has_leakage


def test_has_leakage():
    assert has_leakage([1, 2], [2, 3])
