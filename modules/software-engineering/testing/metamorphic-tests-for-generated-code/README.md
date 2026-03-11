# Metamorphic Tests For Generated Code

> Track: `software-engineering` | Topic: `testing`

## Concept

Metamorphic tests check whether behavior stays consistent under transformations that should preserve a known invariant, which is especially useful when AI-generated code lacks obvious example cases.

## Key Points

- The key question is not only “is this output correct?” but also “does this invariant survive equivalent inputs?”
- Reordering, casing, normalization, and grouping are common invariant-preserving transformations.
- Metamorphic checks often catch subtle regressions that example-based tests miss.

## Minimal Code Mental Model

```python
failures = metamorphic_failures(
    lambda values: sorted_unique(values),
    [["b", "a", "a"], ["a", "b"]],
)
assert failures == []
```

## Function

```python
def sorted_unique(values: list[str]) -> list[str]:
def metamorphic_failures(evaluator, equivalent_inputs: list[list[str]]) -> list[int]:
def preserves_idempotence(values: list[str]) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/testing/metamorphic-tests-for-generated-code/python -q
```
