from batchnorm_transformers import batch_stats


def test_batch_stats():
    mean, var = batch_stats([[1.0, 2.0], [3.0, 4.0]])
    assert mean == 2.5
    assert var > 0.0
