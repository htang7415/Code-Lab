def auc(fpr: list[float], tpr: list[float]) -> float:
    area = 0.0
    for i in range(1, len(fpr)):
        area += (fpr[i] - fpr[i - 1]) * (tpr[i] + tpr[i - 1]) / 2
    return area
