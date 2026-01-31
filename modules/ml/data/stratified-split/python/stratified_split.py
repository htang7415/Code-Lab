from collections import defaultdict


def stratified_split(labels: list[int], train_frac: float) -> tuple[list[int], list[int]]:
    buckets = defaultdict(list)
    for idx, label in enumerate(labels):
        buckets[label].append(idx)
    train, test = [], []
    for idxs in buckets.values():
        cut = int(len(idxs) * train_frac)
        train.extend(idxs[:cut])
        test.extend(idxs[cut:])
    return train, test
