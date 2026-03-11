from __future__ import annotations

from testing_python_services import dependency_overrides, pytest_service_ready, service_test_layers


def test_service_test_layers_expand_with_db_and_external_api_boundaries() -> None:
    assert service_test_layers(needs_db=False, external_api=False) == ["unit"]
    assert service_test_layers(needs_db=True, external_api=True) == ["unit", "db-integration", "contract"]


def test_dependency_overrides_call_out_stubs_and_clock_fixtures() -> None:
    assert dependency_overrides(external_api=True, clock_dependency=True) == ["api-stub", "clock-fixture"]
    assert dependency_overrides(external_api=False, clock_dependency=False) == []


def test_pytest_service_ready_requires_fixtures_and_state_isolation() -> None:
    assert pytest_service_ready(has_fixtures=True, isolates_state=True) is True
    assert pytest_service_ready(has_fixtures=True, isolates_state=False) is False
