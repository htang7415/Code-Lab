from __future__ import annotations


def mean_judge_score(scores: list[float]) -> float:
    if not scores:
        raise ValueError("scores must be non-empty")
    if any(score < 0.0 or score > 1.0 for score in scores):
        raise ValueError("scores must satisfy 0 <= score <= 1")
    return sum(scores) / len(scores)


def trace_grade_packet(run_id: str, judge_score: float, step_statuses: list[str]) -> dict[str, object]:
    cleaned_run_id = run_id.strip()
    if not cleaned_run_id:
        raise ValueError("run_id must be non-empty")
    if judge_score < 0.0 or judge_score > 1.0:
        raise ValueError("judge_score must satisfy 0 <= score <= 1")

    cleaned_statuses = [status.strip().lower() for status in step_statuses if status.strip()]
    if not cleaned_statuses:
        raise ValueError("step_statuses must contain at least one non-empty status")

    blocked_or_failed_steps = sum(
        status in {"blocked", "failed"} for status in cleaned_statuses
    )
    return {
        "run_id": cleaned_run_id,
        "judge_score": judge_score,
        "step_statuses": cleaned_statuses,
        "blocked_or_failed_steps": blocked_or_failed_steps,
    }


def judge_trace_route(judge_score: float, blocked_or_failed_steps: int, threshold: float) -> str:
    if judge_score < 0.0 or judge_score > 1.0:
        raise ValueError("judge_score must satisfy 0 <= score <= 1")
    if threshold < 0.0 or threshold > 1.0:
        raise ValueError("threshold must satisfy 0 <= value <= 1")
    if blocked_or_failed_steps < 0:
        raise ValueError("blocked_or_failed_steps must be non-negative")

    if judge_score < threshold:
        return "fail"
    if blocked_or_failed_steps > 0:
        return "review"
    return "pass"
