from __future__ import annotations

from release_engineering_basics import releasable, release_blockers, required_release_gates


def test_required_release_gates_expand_with_change_scope() -> None:
    assert required_release_gates(["database", "api"]) == [
        "build",
        "tests",
        "rollback-plan",
        "migration-review",
        "compatibility-check",
    ]


def test_release_blockers_find_failed_or_missing_required_gates() -> None:
    gates = required_release_gates(["database"])
    statuses = {"build": "passed", "tests": "passed", "rollback-plan": "passed", "migration-review": "failed"}

    assert release_blockers(gates, statuses) == ["migration-review"]


def test_releasable_requires_every_gate_to_pass() -> None:
    gates = required_release_gates(["api"])
    statuses = {
        "build": "passed",
        "tests": "passed",
        "rollback-plan": "passed",
        "compatibility-check": "passed",
    }

    assert releasable(gates, statuses) is True
    assert releasable(gates, {"build": "passed", "tests": "passed"}) is False
