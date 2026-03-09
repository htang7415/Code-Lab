from __future__ import annotations


def hamming_loss(predictions: list[list[int]], labels: list[list[int]]) -> float:
    if len(predictions) != len(labels):
        raise ValueError("predictions and labels must have the same length")
    if not labels:
        return 0.0

    total_positions = 0
    mismatches = 0

    for prediction_row, label_row in zip(predictions, labels):
        if len(prediction_row) != len(label_row):
            raise ValueError("each prediction row must match its label row length")
        if any(value not in {0, 1} for value in prediction_row + label_row):
            raise ValueError("predictions and labels must be binary")

        total_positions += len(label_row)
        mismatches += sum(prediction != label for prediction, label in zip(prediction_row, label_row))

    return 0.0 if total_positions == 0 else mismatches / total_positions
