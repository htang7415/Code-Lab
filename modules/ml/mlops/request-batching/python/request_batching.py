import math


def batch_requests(n: int, batch_size: int) -> int:
    return math.ceil(n / batch_size)
