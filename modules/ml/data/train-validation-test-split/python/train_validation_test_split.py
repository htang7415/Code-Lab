def split_indices(n: int, train_frac: float, val_frac: float) -> tuple[list[int], list[int], list[int]]:
    n_train = int(n * train_frac)
    n_val = int(n * val_frac)
    train = list(range(0, n_train))
    val = list(range(n_train, n_train + n_val))
    test = list(range(n_train + n_val, n))
    return train, val, test
