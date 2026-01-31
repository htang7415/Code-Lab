# GAN Instability and Mode Collapse

> Track: `ml` | Topic: `generative`

## Concept

Mode collapse happens when the generator outputs limited modes.

## Math

Low diversity ⇒ entropy of samples drops.

## Function

```python
def diversity_score(samples: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/generative/gan-mode-collapse/python -q
```
