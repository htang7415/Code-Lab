from gini_impurity import gini


def test_gini():
    assert gini([0, 0, 1, 1]) == 0.5
