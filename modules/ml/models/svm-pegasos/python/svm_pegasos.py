import torch


def pegasos_kernel_svm(
    data: torch.Tensor,
    labels: torch.Tensor,
    kernel: str = "linear",
    lambda_val: float = 0.01,
    iterations: int = 100,
    sigma: float = 1.0
) -> tuple:
    """
    Deterministic Pegasos for a kernel SVM (full pass over all samples each iteration).

    Uses the exact update rule described:

      eta_t = 1 / (lambda_val * t)

      f(x_i) = sum_j alpha_j * y_j * K(x_j, x_i) + b

      if y_i * f(x_i) < 1:
          alpha_i <- alpha_i + eta_t * (y_i - lambda_val * alpha_i)
          b       <- b + eta_t * y_i

    Args:
        data: (n_samples, n_features) torch tensor OR numpy/array-like
        labels: (n_samples,) torch tensor OR numpy/array-like with values in {-1, +1}
        kernel: 'linear' or 'rbf'
        lambda_val: regularization parameter (lambda > 0)
        iterations: number of iterations (T > 0)
        sigma: RBF bandwidth (sigma > 0), only used if kernel='rbf'

    Returns:
        (alphas, bias) where alphas is a Python list (length n_samples) and bias is float
    """
    X = torch.as_tensor(data, dtype=torch.float64)
    y = torch.as_tensor(labels, dtype=torch.float64).view(-1)

    if X.ndim != 2:
        raise ValueError(f"data must be 2D (n_samples, n_features), got {tuple(X.shape)}")
    n = X.shape[0]
    if y.ndim != 1 or y.shape[0] != n:
        raise ValueError(f"labels must be shape (n_samples,), got {tuple(y.shape)}")
    if kernel not in ("linear", "rbf"):
        raise ValueError("kernel must be 'linear' or 'rbf'")
    if lambda_val <= 0:
        raise ValueError("lambda_val must be > 0")
    if iterations <= 0:
        raise ValueError("iterations must be > 0")
    if kernel == "rbf" and sigma <= 0:
        raise ValueError("sigma must be > 0 for rbf kernel")

    # Precompute kernel matrix K (n x n)
    if kernel == "linear":
        K = X @ X.t()
    else:
        # RBF: exp(-||xi-xj||^2 / (2*sigma^2))
        x2 = (X * X).sum(dim=1, keepdim=True)              # (n,1)
        dist2 = x2 + x2.t() - 2.0 * (X @ X.t())            # (n,n)
        dist2 = torch.clamp(dist2, min=0.0)                # numerical safety
        K = torch.exp(-dist2 / (2.0 * float(sigma) ** 2))

    alpha = torch.zeros(n, dtype=torch.float64)
    b = torch.tensor(0.0, dtype=torch.float64)

    for t in range(1, int(iterations) + 1):
        eta = 1.0 / (float(lambda_val) * t)

        # Deterministic: fixed order, full pass over all samples
        for i in range(n):
            # f(x_i) = sum_j alpha_j * y_j * K(x_j, x_i) + b
            f_i = torch.dot(alpha * y, K[:, i]) + b
            if (y[i] * f_i) < 1.0:
                alpha[i] = alpha[i] + eta * (y[i] - float(lambda_val) * alpha[i])
                b = b + eta * y[i]

    return alpha.tolist(), float(b.item())
