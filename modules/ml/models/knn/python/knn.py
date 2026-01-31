from collections import Counter


def knn_predict(distances: list[float], labels: list[int], k: int) -> int:
    idxs = sorted(range(len(distances)), key=lambda i: distances[i])[:k]
    counts = Counter(labels[i] for i in idxs)
    return counts.most_common(1)[0][0]
