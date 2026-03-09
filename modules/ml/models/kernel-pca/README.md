# Kernel PCA

> Track: `ml` | Topic: `models`

## Concept

Kernel PCA performs PCA in an implicit feature space by building and centering a kernel matrix.
This module focuses on the RBF-kernel construction and centering step.

## Math

$$K_{ij} = \exp(-\gamma \lVert x_i - x_j \rVert^2)$$

$$K_c = K - \mathbf{1}K - K\mathbf{1} + \mathbf{1}K\mathbf{1}$$

- $K$ -- kernel matrix
- $K_c$ -- centered kernel matrix
- $\gamma$ -- RBF bandwidth parameter
- $\mathbf{1}$ -- matrix with entries $\frac{1}{n}$

## Key Points

- The kernel matrix measures similarity instead of raw coordinates.
- Centering is required before eigendecomposition in kernel PCA.
- RBF kernels let PCA capture nonlinear structure.

## Function

```python
def centered_rbf_kernel(points: list[list[float]], gamma: float) -> list[list[float]]:
```

## Run tests

```bash
pytest modules/ml/models/kernel-pca/python -q
```
