from moe_routing import moe_combine


def test_moe_combine():
    experts = [[1.0, 0.0], [0.0, 2.0]]
    out = moe_combine(experts, [0.2, 0.8], k=1)
    assert out == [0.0, 2.0]
