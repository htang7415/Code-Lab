# Preference Learning

> Track: `ml` | Topic: `llm`

## Concept

Preference learning optimizes models with pairwise comparisons between outputs.

## Math

$$\text{Pairwise logistic loss: } L = -\log\left(\sigma(\text{score}_{\text{chosen}} - \text{score}_{\text{rejected}})\right)$$

- $\sigma$ -- sigmoid (logistic) function
- $\mathrm{score}_{\mathrm{chosen}}$ -- score for the preferred output
- $\mathrm{score}_{\mathrm{rejected}}$ -- score for the rejected output
- $L$ -- loss value

## Function

```python
def preference_loss(score_chosen: float, score_rejected: float) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/preference-learning/python -q
```
