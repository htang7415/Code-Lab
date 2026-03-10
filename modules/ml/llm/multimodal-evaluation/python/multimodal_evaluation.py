from __future__ import annotations


def vqa_consensus_accuracy(matching_references: int) -> float:
    if matching_references < 0:
        raise ValueError("matching_references must be non-negative")
    return min(matching_references / 3.0, 1.0)


def modality_coverage_rate(required_modalities: list[str], provided_modalities: list[str]) -> float:
    required = {modality.strip().lower() for modality in required_modalities if modality.strip()}
    provided = {modality.strip().lower() for modality in provided_modalities if modality.strip()}
    if not required:
        return 1.0
    return len(required & provided) / len(required)


def average_multimodal_accuracy(scores: list[float]) -> float:
    if not scores:
        return 0.0
    if any(not 0.0 <= score <= 1.0 for score in scores):
        raise ValueError("scores must satisfy 0 <= value <= 1")
    return sum(scores) / len(scores)
