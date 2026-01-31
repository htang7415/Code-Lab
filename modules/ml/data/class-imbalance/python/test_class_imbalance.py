from class_imbalance import class_weights


def test_class_weights():
    weights = class_weights([0, 0, 1])
    assert weights[1] > weights[0]
