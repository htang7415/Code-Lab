# Spec-First AI Coding

> Track: `software-engineering` | Topic: `tooling`

## Concept

AI-generated code is safer when the model is given an explicit spec with contracts, constraints, and verification targets before it starts producing implementation details.

## Key Points

- A vague prompt creates vague code and vague review scope.
- Specs should name the contract, invariants, and verification path.
- Missing spec sections are a delivery risk, not just a documentation gap.

## Minimal Code Mental Model

```python
missing = missing_spec_sections(required, present)
ready = spec_ready_for_generation(required, present)
focus = review_focus(["api", "mutation", "ai-generated"])
```

## Function

```python
def missing_spec_sections(required_sections: list[str], present_sections: list[str]) -> list[str]:
def spec_ready_for_generation(required_sections: list[str], present_sections: list[str]) -> bool:
def review_focus(change_tags: list[str]) -> list[str]:
```

## Run tests

```bash
pytest modules/software-engineering/tooling/spec-first-ai-coding/python -q
```
