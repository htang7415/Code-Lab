def has_leakage(train_ids: list[int], test_ids: list[int]) -> bool:
    return bool(set(train_ids) & set(test_ids))
