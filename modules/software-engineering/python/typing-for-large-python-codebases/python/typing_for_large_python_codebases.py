from __future__ import annotations


def missing_annotations(params: dict[str, str | None], return_type: str | None) -> list[str]:
    missing = [name for name, annotation in params.items() if annotation is None or not annotation.strip()]
    if return_type is None or not return_type.strip():
        missing.append("return")
    return missing


def typed_api_ready(params: dict[str, str | None], return_type: str | None) -> bool:
    return not missing_annotations(params, return_type)


def needs_protocol(interface_methods: int, multiple_implementations: bool) -> bool:
    if interface_methods < 0:
        raise ValueError("interface_methods must be non-negative")
    return multiple_implementations and interface_methods >= 2
