from decision_trees import gini_impurity


def test_gini_impurity():
    assert gini_impurity([0, 0, 1, 1]) == 0.5
