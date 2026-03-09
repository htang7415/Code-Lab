def gradient_boosting_step(
    targets: list[float],
    predictions: list[float],
    weak_learner_output: list[float],
    learning_rate: float,
) -> tuple[list[float], list[float]]:
    if len(targets) != len(predictions) or len(predictions) != len(weak_learner_output):
        raise ValueError("targets, predictions, and weak_learner_output must have the same length")
    if learning_rate < 0.0:
        raise ValueError("learning_rate must be non-negative")

    updated = [
        pred + learning_rate * stage
        for pred, stage in zip(predictions, weak_learner_output)
    ]
    residuals = [target - pred for target, pred in zip(targets, updated)]
    return updated, residuals
