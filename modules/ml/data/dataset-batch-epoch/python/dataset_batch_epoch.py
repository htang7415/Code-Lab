import math


def num_batches(dataset_size: int, batch_size: int) -> int:
    return math.ceil(dataset_size / batch_size)
