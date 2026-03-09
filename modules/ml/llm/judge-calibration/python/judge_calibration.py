from __future__ import annotations


def judge_calibration_gap(confidences: list[float], correctness: list[int]) -> float:
    if len(confidences) != len(correctness):
        raise ValueError("confidences and correctness must have the same length")
    if any(confidence < 0.0 or confidence > 1.0 for confidence in confidences):
        raise ValueError("confidences must satisfy 0 <= confidence <= 1")
    if any(value not in {0, 1} for value in correctness):
        raise ValueError("correctness must be binary")
    if not confidences:
        return 0.0

    return sum(abs(confidence - value) for confidence, value in zip(confidences, correctness)) / len(confidences)
