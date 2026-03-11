from __future__ import annotations


def missing_spec_sections(required_sections: list[str], present_sections: list[str]) -> list[str]:
    present = {section.strip().lower() for section in present_sections if section.strip()}
    return [
        section
        for section in required_sections
        if section.strip().lower() not in present
    ]


def spec_ready_for_generation(required_sections: list[str], present_sections: list[str]) -> bool:
    return not missing_spec_sections(required_sections, present_sections)


def review_focus(change_tags: list[str]) -> list[str]:
    normalized = {tag.strip().lower() for tag in change_tags if tag.strip()}
    focus: list[str] = ["contract"]
    if normalized.intersection({"api", "schema", "serialization"}):
        focus.append("compatibility")
    if normalized.intersection({"mutation", "workflow", "state"}):
        focus.append("invariants")
    if normalized.intersection({"ai-generated", "automation"}):
        focus.append("regression")
    return focus
