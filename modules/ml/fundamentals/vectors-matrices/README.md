# Vectors and Matrices

> Track: `ml` | Topic: `fundamentals`

## Concept

Vectors represent ordered numeric quantities. Matrices represent linear maps:
they take an input vector, mix its coordinates with weighted sums, and produce
an output vector in the same or a different space.

From first principles, matrix-vector multiplication is just repeated dot
products: each row of the matrix asks, "how much of each input coordinate should
contribute to this output coordinate?"

## Math

$$y = A x$$

- $A \in \mathbb{R}^{m \times n}$ -- transformation matrix
- $x \in \mathbb{R}^{n}$ -- input vector
- $y \in \mathbb{R}^{m}$ -- transformed output vector

## Key Points

- Rows of $A$ define how to compute each output coordinate.
- Columns of $A$ show how each input coordinate influences the outputs.
- Linear maps preserve addition and scalar multiplication, which is why
  matrices are central to ML layers.

## Function

```python
def matvec(a: list[list[float]], x: list[float]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/fundamentals/vectors-matrices/python -q
```
