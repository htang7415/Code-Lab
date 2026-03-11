from __future__ import annotations


def review_checklist(change_tags: list[str]) -> list[str]:
    normalized = {tag.strip().lower() for tag in change_tags if tag.strip()}
    items = ["correctness", "tests"]
    if normalized.intersection({"api", "schema"}):
        items.append("compatibility")
    if normalized.intersection({"security", "auth", "secret"}):
        items.append("security")
    if normalized.intersection({"ai-generated", "automation"}):
        items.append("regression")
    return items


def missing_review_items(required_items: list[str], completed_items: dict[str, bool]) -> list[str]:
    return [
        item
        for item in required_items
        if completed_items.get(item) is not True
    ]


def review_complete(required_items: list[str], completed_items: dict[str, bool]) -> bool:
    return not missing_review_items(required_items, completed_items)
