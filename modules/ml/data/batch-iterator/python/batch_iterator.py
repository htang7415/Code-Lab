def batch_indices(n: int, batch_size: int) -> list[list[int]]:
    batches = []
    for start in range(0, n, batch_size):
        batches.append(list(range(start, min(n, start + batch_size))))
    return batches
