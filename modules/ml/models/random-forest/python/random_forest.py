def bootstrap_indices(n: int, seed: int = 0) -> list[int]:
    idxs = []
    state = seed
    for _ in range(n):
        state = (1103515245 * state + 12345) % (2**31)
        idxs.append(state % n)
    return idxs
