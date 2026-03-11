from __future__ import annotations


def orchestrator_assignments(goal: str, role_to_subtask: dict[str, str]) -> list[dict[str, str]]:
    cleaned_goal = goal.strip()
    if not cleaned_goal:
        raise ValueError("goal must be non-empty")
    if not role_to_subtask:
        raise ValueError("role_to_subtask must be non-empty")

    assignments: list[dict[str, str]] = []
    for worker, subtask in role_to_subtask.items():
        cleaned_worker = worker.strip()
        cleaned_subtask = subtask.strip()
        if not cleaned_worker:
            raise ValueError("worker names must be non-empty")
        if not cleaned_subtask:
            raise ValueError("subtasks must be non-empty")
        assignments.append(
            {
                "goal": cleaned_goal,
                "worker": cleaned_worker,
                "subtask": cleaned_subtask,
            }
        )
    return assignments


def worker_task_packet(
    worker: str,
    subtask: str,
    shared_context: dict[str, object],
    max_steps: int = 1,
) -> dict[str, object]:
    cleaned_worker = worker.strip()
    cleaned_subtask = subtask.strip()
    if not cleaned_worker:
        raise ValueError("worker must be non-empty")
    if not cleaned_subtask:
        raise ValueError("subtask must be non-empty")
    if max_steps <= 0:
        raise ValueError("max_steps must be positive")

    return {
        "worker": cleaned_worker,
        "subtask": cleaned_subtask,
        "shared_context": shared_context,
        "max_steps": max_steps,
    }


def orchestrator_summary(worker_reports: list[dict[str, object]]) -> dict[str, object]:
    done_workers: list[str] = []
    blocked_workers: list[str] = []
    results: dict[str, object] = {}

    for report in worker_reports:
        worker = str(report.get("worker", "")).strip()
        status = str(report.get("status", "")).strip().lower()
        if not worker or not status:
            continue
        if status == "done":
            done_workers.append(worker)
        elif status == "blocked":
            blocked_workers.append(worker)
        results[worker] = report.get("result")

    return {
        "done_workers": done_workers,
        "blocked_workers": blocked_workers,
        "results": results,
        "complete": len(blocked_workers) == 0 and len(done_workers) == len(results),
    }
