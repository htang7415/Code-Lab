# SVM (Pegasos)

> Track: `ml` | Topic: `models`

## Concept

Pegasos can be used in kernel form by maintaining per-sample coefficients $\alpha_i$ and a bias term $b$.

## Math

For iteration $t$:

$$\eta_t = \frac{1}{\lambda t}$$

$$f(x_i) = \sum_j \alpha_j y_j K(x_j, x_i) + b$$

If $y_i f(x_i) < 1$:

$$\alpha_i \leftarrow \alpha_i + \eta_t\left(y_i - \lambda \alpha_i\right),\quad b \leftarrow b + \eta_t y_i$$

- $K(x_j, x_i)$ -- kernel value (linear or RBF)
- $\alpha_i$ -- coefficient for sample $i$
- $b$ -- bias/intercept
- $\lambda$ -- regularization parameter
- $\eta_t$ -- step size at iteration $t$

## Function

```python
def pegasos_kernel_svm(
    data: torch.Tensor,
    labels: torch.Tensor,
    kernel: str = "linear",
    lambda_val: float = 0.01,
    iterations: int = 100,
    sigma: float = 1.0
) -> tuple:
```

## Run tests

```bash
pytest modules/ml/models/svm-pegasos/python -q
```
