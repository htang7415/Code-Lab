from roc_auc import auc


def test_auc():
    assert auc([0.0, 1.0], [0.0, 1.0]) == 0.5
