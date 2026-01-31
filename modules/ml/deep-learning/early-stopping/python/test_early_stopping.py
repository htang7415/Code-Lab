from early_stopping import should_stop


def test_should_stop():
    losses = [1.0, 0.9, 0.91, 0.92]
    assert should_stop(losses, patience=2)
