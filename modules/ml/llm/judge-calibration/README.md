# Judge Calibration

> Track: `ml` | Topic: `llm`

## Concept

Judge calibration asks whether a model judge's confidence tracks whether its verdict is actually correct.

## Math

$$
\mathrm{gap} = \frac{1}{n} \sum_{i=1}^{n} \left| c_i - y_i \right|
$$

- $c_i$ -- judge confidence for example $i$
- $y_i$ -- correctness indicator for the judge's verdict
- $n$ -- number of judged examples

## Key Points

- Lower gap means the judge's reported confidence better matches reality.
- This is a lightweight calibration proxy for judge-style evaluation pipelines.
- It complements judge win-rate metrics by using confidence information too.

## Function

```python
def judge_calibration_gap(confidences: list[float], correctness: list[int]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/judge-calibration/python -q
```
