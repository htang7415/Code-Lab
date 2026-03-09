def roofline(
    flops: float,
    bytes_moved: float,
    peak_flops_per_s: float,
    memory_bandwidth_bytes_per_s: float,
) -> tuple[float, float, str]:
    if flops <= 0 or bytes_moved <= 0 or peak_flops_per_s <= 0 or memory_bandwidth_bytes_per_s <= 0:
        raise ValueError("all arguments must be positive")

    arithmetic_intensity = flops / bytes_moved
    memory_ceiling = arithmetic_intensity * memory_bandwidth_bytes_per_s
    attainable = min(peak_flops_per_s, memory_ceiling)
    bottleneck = "memory" if memory_ceiling < peak_flops_per_s else "compute"
    return arithmetic_intensity, attainable, bottleneck
