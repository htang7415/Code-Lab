# Weight of Evidence

> Track: `ml` | Topic: `data`

## Concept

Weight of evidence (WoE) encodes how strongly a category is associated with the positive class relative to the negative class.

## Math

$$
\mathrm{WoE} = \log \frac{(p + s)/(P + 2s)}{(n + s)/(N + 2s)}
$$

- $p$ -- positive count for the category
- $n$ -- negative count for the category
- $P$ -- total positive count across data
- $N$ -- total negative count across data
- $s$ -- smoothing constant

## Key Points

- WoE is a supervised categorical encoding used in scorecards and linear models.
- Positive values indicate stronger association with the positive class.
- Smoothing avoids undefined logs when a cell count is zero.

## Function

```python
def weight_of_evidence(
    positive_count: int,
    negative_count: int,
    total_positive: int,
    total_negative: int,
    smoothing: float = 0.5,
) -> float:
```

## Run tests

```bash
pytest modules/ml/data/weight-of-evidence/python -q
```
