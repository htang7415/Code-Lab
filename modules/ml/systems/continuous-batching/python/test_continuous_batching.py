from continuous_batching import continuous_batch_step


def test_continuous_batch_step_removes_finished_and_admits_queue():
    active, queue = continuous_batch_step(
        active_requests=[3, 1],
        queued_requests=[4, 2],
        capacity=3,
    )
    assert active == [2, 4, 2]
    assert queue == []


def test_continuous_batch_step_keeps_running_requests_when_queue_empty():
    active, queue = continuous_batch_step(
        active_requests=[2, 2],
        queued_requests=[],
        capacity=3,
    )
    assert active == [1, 1]
    assert queue == []
