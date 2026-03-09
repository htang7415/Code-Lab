from kv_cache import kv_cache_bytes


def test_kv_cache_bytes():
    assert kv_cache_bytes(
        num_layers=2,
        num_tokens=4,
        num_kv_heads=8,
        head_dim=16,
        bytes_per_element=2,
        batch_size=1,
    ) == 4096
