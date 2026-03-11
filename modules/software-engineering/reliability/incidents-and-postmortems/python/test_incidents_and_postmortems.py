from __future__ import annotations

import pytest

from incidents_and_postmortems import (
    incident_severity,
    missing_postmortem_sections,
    postmortem_complete,
)


POSTMORTEM = {
    "summary": "Database pool exhausted under retry storm.",
    "impact": "Checkout failures for 42 minutes.",
    "timeline": "10:00 alert, 10:12 mitigation, 10:42 recovered.",
    "root-cause": "Retries amplified dependency saturation.",
    "actions": "Add retry caps and pool saturation alert.",
}


def test_incident_severity_reflects_user_harm_and_data_loss() -> None:
    assert incident_severity(user_impacting=True, duration_minutes=45, data_loss=False) == "sev1"
    assert incident_severity(user_impacting=True, duration_minutes=10, data_loss=False) == "sev2"
    assert incident_severity(user_impacting=False, duration_minutes=10, data_loss=False) == "sev3"


def test_missing_postmortem_sections_finds_incomplete_writeups() -> None:
    assert missing_postmortem_sections(POSTMORTEM) == []
    assert missing_postmortem_sections({"summary": "Only summary"}) == [
        "actions",
        "impact",
        "root-cause",
        "timeline",
    ]


def test_postmortem_complete_requires_sections_and_action_items() -> None:
    assert postmortem_complete(POSTMORTEM, ["add retry budget alert"]) is True
    assert postmortem_complete(POSTMORTEM, [" ", ""]) is False

    with pytest.raises(ValueError):
        incident_severity(user_impacting=True, duration_minutes=-1, data_loss=False)
