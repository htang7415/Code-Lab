# Pooling (Max/Average)

> Track: `ml` | Topic: `computer-vision`

## Concept

Pooling downsamples a local window of activations into one summary value. This
reduces spatial resolution while preserving a coarse signal about what is
present in the window.

## Math

$$
\begin{aligned}
y_{\max} &= \max_{i \in \mathcal{W}} x_i \\
y_{\text{avg}} &= \frac{1}{|\mathcal{W}|}\sum_{i \in \mathcal{W}} x_i
\end{aligned}
$$

- $\mathcal{W}$ -- pooling window
- $x_i$ -- activation at index $i$ inside the window
- $y_{\max}$ -- max-pooled output
- $y_{\text{avg}}$ -- average-pooled output

## Key Points

- Max pooling keeps the strongest activation.
- Average pooling preserves the mean response of the window.
- Pooling trades spatial precision for translation tolerance and lower compute.

## Function

```python
def max_pool(window: list[float]) -> float:
def avg_pool(window: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/computer-vision/pooling/python -q
```
