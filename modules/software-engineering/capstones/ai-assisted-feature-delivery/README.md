# AI-Assisted Feature Delivery

> Track: `software-engineering` | Topic: `capstones`

## Concept

This capstone combines spec-first prompting, generated-code review gates, regression strength, and rollout readiness into one compact AI-assisted delivery workflow.

## Key Points

- AI should not start implementation before the spec covers contracts, tests, and rollback.
- Review needs explicit blockers for compatibility, security, and regression risk.
- Verification should be strong enough to catch plausible but wrong generated code.
- Shipping still depends on rollback readiness, not just passing tests.

## Minimal Code Mental Model

```python
decision = delivery_decision(
    ["api", "ai-generated"],
    ["contract", "invariants", "tests", "rollback", "compatibility"],
    {"correctness": True, "tests": True, "compatibility": True, "regression": True},
    unit_passed=True,
    regression_passed=True,
    metamorphic_passed=True,
    rollback_ready=True,
)
```

## Function

```python
def required_spec_sections(change_tags: list[str]) -> list[str]:
def spec_gaps(change_tags: list[str], present_sections: list[str]) -> list[str]:
def review_blockers(change_tags: list[str], completed_items: dict[str, bool]) -> list[str]:
def verification_strength(
    unit_passed: bool,
    regression_passed: bool,
    metamorphic_passed: bool,
) -> str:
def delivery_decision(
    change_tags: list[str],
    present_sections: list[str],
    completed_items: dict[str, bool],
    unit_passed: bool,
    regression_passed: bool,
    metamorphic_passed: bool,
    rollback_ready: bool,
) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/capstones/ai-assisted-feature-delivery/python -q
```
