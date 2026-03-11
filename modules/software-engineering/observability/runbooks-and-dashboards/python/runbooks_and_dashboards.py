from __future__ import annotations


DEFAULT_RUNBOOK_FIELDS = ["service", "owner", "page-policy", "health-check", "rollback"]


def missing_runbook_fields(runbook: dict[str, str], required_fields: list[str] | None = None) -> list[str]:
    fields = required_fields or DEFAULT_RUNBOOK_FIELDS
    missing: list[str] = []
    for field in fields:
        cleaned_field = field.strip()
        if not cleaned_field:
            continue
        if not runbook.get(cleaned_field, "").strip():
            missing.append(cleaned_field)
    return sorted(missing)


def missing_dashboard_panels(required_panels: list[str], present_panels: list[str]) -> list[str]:
    required = {panel.strip() for panel in required_panels if panel.strip()}
    present = {panel.strip() for panel in present_panels if panel.strip()}
    return sorted(required - present)


def operator_ready(runbook: dict[str, str], required_panels: list[str], present_panels: list[str]) -> bool:
    return not missing_runbook_fields(runbook) and not missing_dashboard_panels(required_panels, present_panels)
