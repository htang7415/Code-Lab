# PCA

> Track: `ml` | Topic: `fundamentals`

## Concept

PCA finds orthogonal directions (principal components) that explain the most variance.

## Math
For standardized data matrix $Z \in \mathbb{R}^{n \times d}$:

$$C = \frac{1}{n-1} Z^\top Z$$

Then principal components are the top eigenvectors of $C$ (largest eigenvalues first).

- $Z$ -- standardized data matrix
- $C$ -- sample covariance matrix
- $n$ -- number of samples
- $d$ -- number of features

## Function

```python
def pca(data, k) -> torch.Tensor:
```

## Run tests

```bash
pytest modules/ml/fundamentals/pca/python -q
```
