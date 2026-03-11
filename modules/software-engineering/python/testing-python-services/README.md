# Testing Python Services

> Track: `software-engineering` | Topic: `python`

## Concept

Python service tests stay useful when external dependencies are isolated, shared state is controlled, and fixtures make the service boundary easy to exercise.

## Key Points

- Database, clock, and external API dependencies should be isolated in tests.
- Service tests should prefer fast fixtures over broad environment coupling.
- A Python service test suite becomes fragile when state leaks across test cases.

## Minimal Code Mental Model

```python
layers = service_test_layers(needs_db=True, external_api=True)
overrides = dependency_overrides(external_api=True, clock_dependency=True)
ready = pytest_service_ready(has_fixtures=True, isolates_state=True)
```

## Function

```python
def service_test_layers(needs_db: bool, external_api: bool) -> list[str]:
def dependency_overrides(external_api: bool, clock_dependency: bool) -> list[str]:
def pytest_service_ready(has_fixtures: bool, isolates_state: bool) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/python/testing-python-services/python -q
```
