def split_gain(
    left_grad: float,
    left_hess: float,
    right_grad: float,
    right_hess: float,
    lambda_reg: float,
    gamma: float,
) -> float:
    if left_hess < 0.0 or right_hess < 0.0 or lambda_reg < 0.0:
        raise ValueError("hessians and lambda_reg must be non-negative")

    parent_grad = left_grad + right_grad
    parent_hess = left_hess + right_hess

    left_term = (left_grad ** 2) / (left_hess + lambda_reg)
    right_term = (right_grad ** 2) / (right_hess + lambda_reg)
    parent_term = (parent_grad ** 2) / (parent_hess + lambda_reg)
    return 0.5 * (left_term + right_term - parent_term) - gamma
