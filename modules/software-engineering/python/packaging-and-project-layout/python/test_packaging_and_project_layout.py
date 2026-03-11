from __future__ import annotations

import pytest

from packaging_and_project_layout import import_root, packaging_ready, recommended_paths


def test_recommended_paths_reflect_src_layout_choice() -> None:
    assert recommended_paths("billing_service", uses_src_layout=True) == {
        "package_root": "src/billing_service",
        "tests": "tests",
        "config": "pyproject.toml",
    }
    assert import_root("billing_service", uses_src_layout=False) == "billing_service"


def test_packaging_ready_requires_basic_project_structure() -> None:
    assert packaging_ready(pyproject_present=True, package_init_present=True, tests_present=True) is True
    assert packaging_ready(pyproject_present=True, package_init_present=False, tests_present=True) is False


def test_package_name_must_be_non_empty() -> None:
    with pytest.raises(ValueError):
        recommended_paths(" ", uses_src_layout=True)
