from __future__ import annotations


def evaluation_report(check_results: dict[str, bool]) -> dict[str, object]:
    if not check_results:
        raise ValueError("check_results must be non-empty")

    passed_checks = [name for name, passed in check_results.items() if passed]
    failed_checks = [name for name, passed in check_results.items() if not passed]
    return {
        "passed": len(failed_checks) == 0,
        "passed_checks": passed_checks,
        "failed_checks": failed_checks,
        "score": len(passed_checks) / len(check_results),
    }


def optimizer_route(passed: bool, attempt: int, max_attempts: int) -> str:
    if attempt < 0:
        raise ValueError("attempt must be non-negative")
    if max_attempts <= 0:
        raise ValueError("max_attempts must be positive")
    if passed:
        return "accept"
    if attempt + 1 < max_attempts:
        return "revise"
    return "escalate"


def revision_packet(draft: str, failed_checks: list[str]) -> dict[str, object]:
    cleaned_draft = draft.strip()
    if not cleaned_draft:
        raise ValueError("draft must be non-empty")
    if not failed_checks:
        raise ValueError("failed_checks must be non-empty")

    normalized_checks = [check.strip() for check in failed_checks if check.strip()]
    if not normalized_checks:
        raise ValueError("failed_checks must include at least one non-empty check")

    return {
        "draft": cleaned_draft,
        "feedback": normalized_checks,
    }
