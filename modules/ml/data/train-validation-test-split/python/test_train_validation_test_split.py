from train_validation_test_split import split_indices


def test_split_indices():
    train, val, test = split_indices(10, 0.6, 0.2)
    assert len(train) == 6
    assert len(val) == 2
    assert len(test) == 2
