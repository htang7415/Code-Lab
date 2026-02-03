# Pooling (Max/Average)

> Track: `ml` | Topic: `computer-vision`

## Concept

Pooling downsamples by taking max or average over windows.

## Math

$$
\begin{aligned}
y_{\max} &= \max_{i \in \mathcal{W}} x_i \\
y_{\text{avg}} &= \frac{1}{|\mathcal{W}|}\sum_{i \in \mathcal{W}} x_i
\end{aligned}
$$

- $x_i$ -- i-th input (feature vector or sample)
- $y$ -- target/label
- $i$ -- index
- $x$ -- input (feature vector or sample)

## Function

```python
def max_pool(window: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/computer-vision/pooling/python -q
```
