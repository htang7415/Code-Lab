from __future__ import annotations


def benchmark_manifest(case_buckets: list[str]) -> dict[str, object]:
    if not case_buckets:
        raise ValueError("case_buckets must be non-empty")

    bucket_counts: dict[str, int] = {}
    for bucket in case_buckets:
        cleaned_bucket = bucket.strip()
        if not cleaned_bucket:
            raise ValueError("bucket names must be non-empty")
        bucket_counts[cleaned_bucket] = bucket_counts.get(cleaned_bucket, 0) + 1

    return {
        "total_cases": len(case_buckets),
        "bucket_counts": bucket_counts,
    }


def baseline_snapshot(name: str, metrics: dict[str, float]) -> dict[str, object]:
    cleaned_name = name.strip()
    if not cleaned_name:
        raise ValueError("name must be non-empty")
    if not metrics:
        raise ValueError("metrics must be non-empty")
    return {
        "name": cleaned_name,
        "metrics": metrics,
        "frozen": True,
    }


def benchmark_gate(
    candidate_success: float,
    baseline_success: float,
    min_success: float,
    max_drop: float,
) -> str:
    values = [candidate_success, baseline_success, min_success]
    if any(not 0.0 <= value <= 1.0 for value in values):
        raise ValueError("success metrics must satisfy 0 <= value <= 1")
    if max_drop < 0.0:
        raise ValueError("max_drop must be non-negative")

    if candidate_success < min_success:
        return "fail"
    if baseline_success - candidate_success > max_drop:
        return "review"
    return "pass"
