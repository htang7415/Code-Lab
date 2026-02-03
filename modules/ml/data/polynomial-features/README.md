# Polynomial Feature Expansion

> Track: `ml` | Topic: `data`

## Concept

Polynomial feature expansion creates higher-order terms (powers and interactions) from the original input features, enabling linear models to capture nonlinear relationships. For a single feature $x$ and degree $d$, the expansion produces the vector $[x, x^2, \ldots, x^d]$. For multiple features, it also generates all cross-product interaction terms up to the specified degree.

This technique is valuable because it allows the well-understood and computationally efficient linear regression framework to fit curves, surfaces, and complex decision boundaries. However, the number of generated features grows combinatorially with the number of input features and the degree, which can lead to overfitting and high computational cost. Pairing polynomial expansion with regularization (e.g., Ridge or Lasso) is essential for controlling model complexity.

## Math

For a single feature $x$ with degree $d$:

$$\phi(x) = \bigl[x, \; x^2, \; \ldots, \; x^d\bigr]$$

For two features $x_1, x_2$ with degree $d = 2$:

$$\phi(x_1, x_2) = \bigl[1, \; x_1, \; x_2, \; x_1^2, \; x_1 x_2, \; x_2^2\bigr]$$

The total number of features for $p$ original features and degree $d$ (including the bias term) is:

$$\binom{p + d}{d}$$

- $x$ -- original input feature
- $d$ -- maximum polynomial degree
- $p$ -- number of original input features
- $\phi$ -- feature mapping from the original space to the expanded space

- $x_1$ -- input (feature vector or sample) at index 1
- $x_2$ -- input (feature vector or sample) at index 2

## Key Points

- Feature count grows combinatorially: with $p = 10$ features and $d = 3$, the expansion produces $\binom{13}{3} = 286$ features.
- Always pair polynomial expansion with regularization to prevent overfitting in the high-dimensional feature space.
- For a single feature, polynomial expansion is equivalent to fitting a degree-$d$ polynomial curve.
- Interaction terms (e.g., $x_1 x_2$) capture relationships between features that pure power terms miss.

## Function

```python
def poly_features(x: float, degree: int) -> list[float]:
```

- `x` -- scalar input value to expand
- `degree` -- maximum polynomial degree $d$

## Run tests

```bash
pytest modules/ml/data/polynomial-features/python -q
```
