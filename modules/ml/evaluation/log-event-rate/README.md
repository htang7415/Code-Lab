# Log Event Rate

> Track: `ml` | Topic: `evaluation`

## Concept

Log event rate is the logarithm of a single positive event rate.

## Math

$$
\log \mathrm{EventRate} = \log\left(\frac{e}{n}\right)
$$

- $e$ -- event count
- $n$ -- total count

## Key Points

- This compresses rates onto a log scale.
- Larger negative values correspond to rarer events.
- This module returns negative infinity when the event rate is zero.

## Function

```python
def log_event_rate(event_count: int, total_count: int) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/log-event-rate/python -q
```
