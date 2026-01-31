# Choose GAN vs VAE vs Diffusion

> Track: `ml` | Topic: `generative`

## Concept

Pick a model based on fidelity, diversity, and speed trade-offs.

## Math

Selection is heuristic, not a fixed formula.

## Function

```python
def choose_model(priority: str) -> str:
```

## Run tests

```bash
pytest modules/ml/generative/model-selection/python -q
```
