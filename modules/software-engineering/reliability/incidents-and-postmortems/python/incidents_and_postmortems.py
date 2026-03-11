from __future__ import annotations


DEFAULT_SECTIONS = ["summary", "impact", "timeline", "root-cause", "actions"]


def incident_severity(user_impacting: bool, duration_minutes: int, data_loss: bool) -> str:
    if duration_minutes < 0:
        raise ValueError("duration_minutes must be non-negative")
    if data_loss:
        return "sev1"
    if user_impacting and duration_minutes >= 30:
        return "sev1"
    if user_impacting:
        return "sev2"
    return "sev3"


def missing_postmortem_sections(
    postmortem: dict[str, str],
    required_sections: list[str] | None = None,
) -> list[str]:
    sections = required_sections or DEFAULT_SECTIONS
    missing: list[str] = []
    for section in sections:
        cleaned_section = section.strip()
        if not cleaned_section:
            continue
        if not postmortem.get(cleaned_section, "").strip():
            missing.append(cleaned_section)
    return sorted(missing)


def postmortem_complete(postmortem: dict[str, str], action_items: list[str]) -> bool:
    has_actions = any(item.strip() for item in action_items)
    return not missing_postmortem_sections(postmortem) and has_actions
