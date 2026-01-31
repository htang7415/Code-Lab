# RLHF (Reward Model Loss)

> Track: `ml` | Topic: `llm`

## Concept

RLHF uses a reward model trained on preference pairs before policy optimization.

## Math

$$\text{Reward model loss uses the pairwise logistic objective.}$$

## Function

```python
def reward_model_loss(chosen: float, rejected: float) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/rlhf/python -q
```
