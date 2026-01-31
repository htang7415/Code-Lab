# Stratified Split

> Track: `ml` | Topic: `data`

## Concept

Stratified splits preserve class proportions across splits.

## Math

Sample indices per class with same ratio.

## Function

```python
def stratified_split(labels: list[int], train_frac: float) -> tuple[list[int], list[int]]:
```

## Run tests

```bash
pytest modules/ml/data/stratified-split/python -q
```
