# MMLU-Style Evaluation

> Track: `ml` | Topic: `llm`

## Concept

MMLU-style evaluation scores multiple-choice questions by checking whether the predicted answer option matches the gold option.
This module focuses on normalized answer matching.

## Math

$$\mathrm{accuracy} = \frac{1}{n} \sum_{i=1}^{n} \mathbb{I}[\hat{y}_i = y_i]$$

- $n$ -- number of questions
- $\hat{y}_i$ -- predicted option for question $i$
- $y_i$ -- gold option for question $i$

## Key Points

- Multiple-choice benchmark scoring is usually exact, not fuzzy.
- Normalization matters because model outputs may contain lowercase letters or extra spaces.
- This metric measures final answer selection, not confidence calibration.

## Function

```python
def mmlu_accuracy(predictions: list[str], labels: list[str]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/mmlu-evaluation/python -q
```
