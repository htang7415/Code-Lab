def continuous_batch_step(
    active_requests: list[int],
    queued_requests: list[int],
    capacity: int,
) -> tuple[list[int], list[int]]:
    if capacity <= 0:
        raise ValueError("capacity must be positive")
    if len(active_requests) > capacity:
        raise ValueError("active_requests cannot exceed capacity")
    if any(steps <= 0 for steps in active_requests + queued_requests):
        raise ValueError("request lengths must be positive")

    next_active = [steps - 1 for steps in active_requests if steps - 1 > 0]
    next_queue = queued_requests[:]

    open_slots = capacity - len(next_active)
    admitted = next_queue[:open_slots]
    next_active.extend(admitted)
    next_queue = next_queue[open_slots:]
    return next_active, next_queue
