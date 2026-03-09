def _normalize_choice(choice: str) -> str:
    return choice.strip().upper()


def mmlu_accuracy(predictions: list[str], labels: list[str]) -> float:
    if len(predictions) != len(labels):
        raise ValueError("predictions and labels must have the same length")
    if not labels:
        raise ValueError("labels must be non-empty")

    correct = sum(
        int(_normalize_choice(prediction) == _normalize_choice(label))
        for prediction, label in zip(predictions, labels)
    )
    return correct / len(labels)
