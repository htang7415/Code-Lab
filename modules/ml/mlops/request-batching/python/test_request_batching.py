from request_batching import batch_requests


def test_batch_requests():
    assert batch_requests(9, 4) == 3
