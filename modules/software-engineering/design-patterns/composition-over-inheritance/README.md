# Composition Over Inheritance

> Track: `software-engineering` | Topic: `design-patterns`

## Concept

Composition combines a few small behaviors directly instead of building subclass trees for every feature combination.

## Key Points

- Orthogonal behaviors combine more cleanly as functions than as subclass matrices.
- Composed steps keep each transformation obvious in code review.
- Use inheritance only when subtype behavior is actually the point.

## Minimal Code Mental Model

```python
label = compose_label(
    "  critical incident  ",
    [normalize_label, str.title, badge("P1")],
)
assert label == "Critical Incident [P1]"
```

## Function

```python
def normalize_label(value: str) -> str:
def badge(label: str):
def compose_label(value: str, transforms) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/design-patterns/composition-over-inheritance/python -q
```
