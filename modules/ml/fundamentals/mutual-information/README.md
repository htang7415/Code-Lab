# Mutual Information

> Track: `ml` | Topic: `fundamentals`

## Concept

Mutual information measures how much knowing one random variable reduces
uncertainty about another. If observing $X$ makes $Y$ easier to predict, then
$I(X;Y)$ is positive. If $X$ and $Y$ are independent, it is zero.

## Math

$$I(X;Y)=\sum_{x,y} p(x,y)\log\left(\frac{p(x,y)}{p(x)p(y)}\right)$$

- $I(X;Y)$ -- mutual information between random variables $X$ and $Y$
- $X, Y$ -- random variables
- $x, y$ -- concrete values taken by those variables
- $p(x,y)$ -- joint probability
- $p(x), p(y)$ -- marginal probabilities

## Key Points

- Mutual information is symmetric: $I(X;Y) = I(Y;X)$.
- It measures statistical dependence, not causal direction.
- The ratio inside the log compares "observed together" to "what independence
  would predict."

## Function

```python
def mutual_information(joint: list[list[float]]) -> float:
```

## Run tests

```bash
pytest modules/ml/fundamentals/mutual-information/python -q
```
