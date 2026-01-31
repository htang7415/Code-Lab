from collections import Counter


def gini_impurity(labels: list[int]) -> float:
    counts = Counter(labels)
    n = len(labels)
    return 1 - sum((c / n) ** 2 for c in counts.values())
