import torch

from pca import pca


def test_pca_top_component():
    data = torch.tensor([[1.0, 1.0], [2.0, 2.0], [3.0, 3.0]], dtype=torch.float32)
    pcs = pca(data, 1)
    expected = torch.tensor([[0.7071], [0.7071]], dtype=torch.float32)
    assert torch.allclose(pcs, expected, atol=1e-4)
