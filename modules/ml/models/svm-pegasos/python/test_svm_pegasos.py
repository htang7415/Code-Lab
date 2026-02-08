import torch

from svm_pegasos import pegasos_kernel_svm


def test_pegasos_kernel_svm_linear_one_iteration():
    data = torch.tensor([[1.0, 0.0], [-1.0, 0.0]], dtype=torch.float64)
    labels = torch.tensor([1.0, -1.0], dtype=torch.float64)
    alphas, bias = pegasos_kernel_svm(data, labels, kernel="linear", lambda_val=1.0, iterations=1)
    assert alphas == [1.0, -1.0]
    assert bias == 0.0
