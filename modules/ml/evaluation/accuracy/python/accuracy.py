def accuracy(y_true: list[int], y_pred: list[int]) -> float:
    correct = sum(1 for a, b in zip(y_true, y_pred) if a == b)
    return correct / len(y_true)
