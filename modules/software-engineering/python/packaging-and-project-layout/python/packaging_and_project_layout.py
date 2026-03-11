from __future__ import annotations


def recommended_paths(package_name: str, uses_src_layout: bool) -> dict[str, str]:
    cleaned_name = package_name.strip()
    if not cleaned_name:
        raise ValueError("package_name must be non-empty")
    prefix = "src/" if uses_src_layout else ""
    return {
        "package_root": f"{prefix}{cleaned_name}",
        "tests": "tests",
        "config": "pyproject.toml",
    }


def import_root(package_name: str, uses_src_layout: bool) -> str:
    return recommended_paths(package_name, uses_src_layout)["package_root"]


def packaging_ready(pyproject_present: bool, package_init_present: bool, tests_present: bool) -> bool:
    return pyproject_present and package_init_present and tests_present
