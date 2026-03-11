from __future__ import annotations


def required_spec_sections(change_tags: list[str]) -> list[str]:
    normalized = {tag.strip().lower() for tag in change_tags if tag.strip()}
    sections = ["contract", "invariants", "tests", "rollback"]
    if normalized.intersection({"api", "schema", "serialization"}):
        sections.append("compatibility")
    if normalized.intersection({"security", "auth", "secret"}):
        sections.append("security")
    if normalized.intersection({"rollout", "migration", "user-facing"}):
        sections.append("observability")
    return sections


def spec_gaps(change_tags: list[str], present_sections: list[str]) -> list[str]:
    present = {section.strip().lower() for section in present_sections if section.strip()}
    return [
        section
        for section in required_spec_sections(change_tags)
        if section not in present
    ]


def review_blockers(change_tags: list[str], completed_items: dict[str, bool]) -> list[str]:
    normalized = {tag.strip().lower() for tag in change_tags if tag.strip()}
    required = ["correctness", "tests"]
    if normalized.intersection({"api", "schema"}):
        required.append("compatibility")
    if normalized.intersection({"security", "auth", "secret"}):
        required.append("security")
    if normalized.intersection({"ai-generated", "automation"}):
        required.append("regression")
    return [
        item
        for item in required
        if completed_items.get(item) is not True
    ]


def verification_strength(
    unit_passed: bool,
    regression_passed: bool,
    metamorphic_passed: bool,
) -> str:
    if unit_passed and regression_passed and metamorphic_passed:
        return "strong"
    if unit_passed and regression_passed:
        return "medium"
    return "weak"


def delivery_decision(
    change_tags: list[str],
    present_sections: list[str],
    completed_items: dict[str, bool],
    unit_passed: bool,
    regression_passed: bool,
    metamorphic_passed: bool,
    rollback_ready: bool,
) -> str:
    if spec_gaps(change_tags, present_sections):
        return "write-spec"
    if review_blockers(change_tags, completed_items):
        return "finish-review"
    if verification_strength(unit_passed, regression_passed, metamorphic_passed) != "strong":
        return "fix-verification"
    if not rollback_ready:
        return "hold"
    return "ship-canary"
