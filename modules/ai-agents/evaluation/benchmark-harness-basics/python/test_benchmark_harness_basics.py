from __future__ import annotations

import pytest

from benchmark_harness_basics import (
    baseline_snapshot,
    benchmark_gate,
    benchmark_manifest,
)


def test_benchmark_harness_builds_manifest_and_baseline_snapshot() -> None:
    assert benchmark_manifest(["tool-use", "tool-use", "planning", "guardrails"]) == {
        "total_cases": 4,
        "bucket_counts": {
            "tool-use": 2,
            "planning": 1,
            "guardrails": 1,
        },
    }
    assert baseline_snapshot("agent-v1", {"success": 0.78, "latency_ms": 140.0}) == {
        "name": "agent-v1",
        "metrics": {"success": 0.78, "latency_ms": 140.0},
        "frozen": True,
    }


def test_benchmark_gate_distinguishes_pass_review_and_fail() -> None:
    assert benchmark_gate(candidate_success=0.79, baseline_success=0.78, min_success=0.75, max_drop=0.03) == "pass"
    assert benchmark_gate(candidate_success=0.74, baseline_success=0.78, min_success=0.75, max_drop=0.03) == "fail"
    assert benchmark_gate(candidate_success=0.76, baseline_success=0.81, min_success=0.75, max_drop=0.03) == "review"


def test_benchmark_harness_validation() -> None:
    with pytest.raises(ValueError):
        benchmark_manifest([])
    with pytest.raises(ValueError):
        baseline_snapshot("", {"success": 0.8})
    with pytest.raises(ValueError):
        benchmark_gate(candidate_success=1.1, baseline_success=0.8, min_success=0.75, max_drop=0.03)
    with pytest.raises(ValueError):
        benchmark_gate(candidate_success=0.8, baseline_success=0.8, min_success=0.75, max_drop=-0.01)
