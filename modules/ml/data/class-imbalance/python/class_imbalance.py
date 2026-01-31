from collections import Counter


def class_weights(labels: list[int]) -> dict[int, float]:
    counts = Counter(labels)
    n = len(labels)
    k = len(counts)
    return {cls: n / (k * cnt) for cls, cnt in counts.items()}
