from __future__ import annotations


def _validate_sample_rate(sample_rate: float) -> None:
    if not 0.0 <= sample_rate <= 1.0:
        raise ValueError("sample_rate must be between 0 and 1")


def _run_fraction(run_id: str) -> float:
    if not run_id.strip():
        raise ValueError("run_id must be non-empty")
    bucket = sum(ord(ch) for ch in run_id) % 10_000
    return bucket / 10_000.0


def should_sample_run(run_id: str, sample_rate: float) -> bool:
    _validate_sample_rate(sample_rate)
    return _run_fraction(run_id) < sample_rate


def sampled_run_ids(run_ids: list[str], sample_rate: float) -> list[str]:
    _validate_sample_rate(sample_rate)
    return [run_id for run_id in run_ids if should_sample_run(run_id, sample_rate)]


def realized_sample_rate(run_ids: list[str], sample_rate: float) -> float:
    _validate_sample_rate(sample_rate)
    if not run_ids:
        return 0.0
    sampled = sampled_run_ids(run_ids, sample_rate)
    return len(sampled) / len(run_ids)
