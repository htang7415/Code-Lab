from __future__ import annotations


def expected_calibration_error(
    confidences: list[float],
    predictions: list[int],
    labels: list[int],
    num_bins: int = 10,
) -> float:
    if len(confidences) != len(predictions) or len(predictions) != len(labels):
        raise ValueError("confidences, predictions, and labels must have the same length")
    if num_bins <= 0:
        raise ValueError("num_bins must be positive")
    if not confidences:
        return 0.0

    bins: list[list[tuple[float, int]]] = [[] for _ in range(num_bins)]
    for confidence, prediction, label in zip(confidences, predictions, labels):
        if not 0.0 <= confidence <= 1.0:
            raise ValueError("confidence values must be between 0 and 1")
        index = min(num_bins - 1, int(confidence * num_bins))
        bins[index].append((confidence, int(prediction == label)))

    total = len(confidences)
    error = 0.0
    for bucket in bins:
        if not bucket:
            continue
        avg_confidence = sum(confidence for confidence, _ in bucket) / len(bucket)
        avg_accuracy = sum(correct for _, correct in bucket) / len(bucket)
        error += (len(bucket) / total) * abs(avg_accuracy - avg_confidence)
    return error


def brier_score(labels: list[int], probabilities: list[float]) -> float:
    if len(labels) != len(probabilities):
        raise ValueError("labels and probabilities must have the same length")
    if any(label not in (0, 1) for label in labels):
        raise ValueError("labels must be binary")
    if any(probability < 0.0 or probability > 1.0 for probability in probabilities):
        raise ValueError("probabilities must satisfy 0 <= p <= 1")
    if not labels:
        return 0.0
    return sum((probability - label) ** 2 for label, probability in zip(labels, probabilities)) / len(labels)


def isotonic_calibration(scores: list[float], labels: list[int]) -> list[float]:
    if len(scores) != len(labels):
        raise ValueError("scores and labels must have the same length")
    if any(label not in {0, 1} for label in labels):
        raise ValueError("labels must be binary")
    if not scores:
        return []

    order = sorted(range(len(scores)), key=lambda index: scores[index])
    blocks: list[dict[str, object]] = []
    for index in order:
        blocks.append({"indices": [index], "sum": float(labels[index]), "count": 1})
        while len(blocks) >= 2:
            previous = blocks[-2]
            current = blocks[-1]
            previous_mean = previous["sum"] / previous["count"]
            current_mean = current["sum"] / current["count"]
            if previous_mean <= current_mean:
                break
            previous["indices"].extend(current["indices"])
            previous["sum"] += current["sum"]
            previous["count"] += current["count"]
            blocks.pop()

    calibrated = [0.0] * len(scores)
    for block in blocks:
        mean_value = block["sum"] / block["count"]
        for index in block["indices"]:
            calibrated[index] = mean_value
    return calibrated
