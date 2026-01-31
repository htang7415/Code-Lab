from batch_iterator import batch_indices


def test_batch_indices():
    batches = batch_indices(5, 2)
    assert batches == [[0, 1], [2, 3], [4]]
