from __future__ import annotations


def service_test_layers(needs_db: bool, external_api: bool) -> list[str]:
    layers = ["unit"]
    if needs_db:
        layers.append("db-integration")
    if external_api:
        layers.append("contract")
    return layers


def dependency_overrides(external_api: bool, clock_dependency: bool) -> list[str]:
    overrides: list[str] = []
    if external_api:
        overrides.append("api-stub")
    if clock_dependency:
        overrides.append("clock-fixture")
    return overrides


def pytest_service_ready(has_fixtures: bool, isolates_state: bool) -> bool:
    return has_fixtures and isolates_state
