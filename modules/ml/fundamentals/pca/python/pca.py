import torch
import numpy as np


def pca(data, k) -> torch.Tensor:
    """
    Perform PCA on `data`, returning the top `k` principal components as a tensor.

    Steps:
      1) Standardize features (zero mean, unit std; ddof=1 for sample std)
      2) Covariance matrix of standardized data
      3) Eigendecomposition via np.linalg.eigh (symmetric, stable)
      4) Sort by descending eigenvalue, take top-k eigenvectors
      5) Apply sign convention: if first |entry|>1e-10 is negative, flip vector
      6) Return torch tensor (n_features, k), rounded to 4 decimals

    Input:
      data: Tensor-like, shape (n_samples, n_features)
      k: int, number of principal components

    Returns:
      torch.Tensor of shape (n_features, k), dtype float32, rounded to 4 decimals.
    """
    # Convert to numpy (float64 for stability)
    X = data.detach().cpu().numpy() if isinstance(data, torch.Tensor) else np.asarray(data)
    if X.ndim != 2:
        raise ValueError(f"data must be 2D (n_samples, n_features), got shape {X.shape}")
    n_samples, n_features = X.shape
    if not (1 <= k <= n_features):
        raise ValueError(f"k must be in [1, n_features={n_features}], got {k}")
    if n_samples < 2:
        raise ValueError("Need at least 2 samples to compute sample covariance (ddof=1).")

    X = X.astype(np.float64, copy=False)

    # 1) Standardize columns
    mean = X.mean(axis=0)
    Xc = X - mean
    std = Xc.std(axis=0, ddof=1)
    # Avoid division by zero for constant features
    std_safe = np.where(std > 0, std, 1.0)
    Z = Xc / std_safe

    # 2) Covariance matrix (features x features), sample covariance
    C = (Z.T @ Z) / (n_samples - 1)

    # 3) Eigendecomposition (ascending eigenvalues)
    evals, evecs = np.linalg.eigh(C)  # evecs columns are eigenvectors

    # 4) Sort by descending eigenvalue and select top-k
    idx = np.argsort(evals)[::-1]
    evecs = evecs[:, idx]
    pcs = evecs[:, :k]  # (n_features, k)

    # 5) Sign convention per eigenvector
    tol = 1e-10
    for j in range(k):
        v = pcs[:, j]
        nz = np.where(np.abs(v) > tol)[0]
        if nz.size > 0 and v[nz[0]] < 0:
            pcs[:, j] = -v

    # 6) Return torch tensor rounded to 4 decimals
    pcs_t = torch.tensor(pcs, dtype=torch.float32)
    pcs_t = torch.round(pcs_t * 1e4) / 1e4
    return pcs_t
