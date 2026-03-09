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
        correct = int(prediction == label)
        bins[index].append((confidence, correct))

    total = len(confidences)
    error = 0.0
    for bucket in bins:
        if not bucket:
            continue
        avg_confidence = sum(confidence for confidence, _ in bucket) / len(bucket)
        avg_accuracy = sum(correct for _, correct in bucket) / len(bucket)
        error += (len(bucket) / total) * abs(avg_accuracy - avg_confidence)
    return error
