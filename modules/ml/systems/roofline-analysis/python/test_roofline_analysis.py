from roofline_analysis import roofline


def test_roofline_memory_bound():
    intensity, attainable, bottleneck = roofline(
        flops=1000.0,
        bytes_moved=500.0,
        peak_flops_per_s=1000.0,
        memory_bandwidth_bytes_per_s=100.0,
    )
    assert intensity == 2.0
    assert attainable == 200.0
    assert bottleneck == "memory"


def test_roofline_compute_bound():
    _, attainable, bottleneck = roofline(
        flops=1000.0,
        bytes_moved=100.0,
        peak_flops_per_s=500.0,
        memory_bandwidth_bytes_per_s=100.0,
    )
    assert attainable == 500.0
    assert bottleneck == "compute"
