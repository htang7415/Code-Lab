# Forward Pass

> Track: `ml` | Topic: `systems`

## Concept

Forward pass computes model outputs from inputs.

## Math

$$y = W x + b$$

## Function

```python
def forward(x: list[float], w: list[float], b: float) -> float:
```

## Run tests

```bash
pytest modules/ml/systems/forward-pass/python -q
```
