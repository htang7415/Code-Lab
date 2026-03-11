from __future__ import annotations

from composition_over_inheritance import badge, compose_label, normalize_label


def test_compose_label_combines_small_behaviors() -> None:
    assert compose_label("  critical incident  ", [normalize_label, str.title, badge("P1")]) == "Critical Incident [P1]"


def test_compose_label_supports_different_variants_without_new_classes() -> None:
    assert compose_label(" api latency ", [normalize_label, str.upper]) == "API LATENCY"
    assert compose_label(" api latency ", [normalize_label, badge("warn")]) == "api latency [warn]"


def test_compose_label_returns_original_value_when_no_transforms_are_supplied() -> None:
    assert compose_label("raw", []) == "raw"
