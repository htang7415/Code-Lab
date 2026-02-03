# RLHF (Reward Model Loss)

> Track: `ml` | Topic: `llm`

## Concept

RLHF uses a reward model trained on preference pairs before policy optimization.

## Math
$$L = -\log \sigma(r_\theta(x^+) - r_\theta(x^-))$$

- $\sigma$ -- sigmoid (logistic) function
- $r_\theta(x)$ -- reward model score
- $x^+$ -- preferred input
- $x^-$ -- rejected input
- $\theta$ -- model parameters
- $L$ -- loss value

## Function

```python
def reward_model_loss(chosen: float, rejected: float) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/rlhf/python -q
```
