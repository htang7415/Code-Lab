from matthews_correlation import mcc


def test_mcc():
    assert mcc(1, 1, 0, 0) == 1.0
