from __future__ import annotations

from rollback_readiness import rollback_blockers, rollback_ready, rollback_risk


def test_rollback_blockers_make_missing_safety_mechanisms_explicit() -> None:
    assert rollback_blockers(flagged=True, reversible_schema=False, canary=True) == [
        "irreversible-schema"
    ]


def test_rollback_ready_requires_all_reversal_paths() -> None:
    assert rollback_ready(flagged=True, reversible_schema=True, canary=True) is True
    assert rollback_ready(flagged=False, reversible_schema=True, canary=True) is False


def test_rollback_risk_grows_with_missing_controls() -> None:
    assert rollback_risk(flagged=True, reversible_schema=True, canary=True) == "low"
    assert rollback_risk(flagged=False, reversible_schema=True, canary=True) == "medium"
    assert rollback_risk(flagged=False, reversible_schema=False, canary=True) == "high"
