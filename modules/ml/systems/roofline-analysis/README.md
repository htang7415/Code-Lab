# Roofline Analysis

> Track: `ml` | Topic: `systems`

## Concept

Roofline analysis relates arithmetic intensity to hardware limits to estimate whether a workload is compute-bound or memory-bound.

## Math

$$I = \frac{F}{Q}$$

$$P_{\max} = \min \left( P_{\text{peak}}, I \cdot BW \right)$$

- $I$ -- arithmetic intensity in FLOPs per byte
- $F$ -- total floating-point operations
- $Q$ -- total bytes moved
- $P_{\text{peak}}$ -- peak compute throughput
- $BW$ -- memory bandwidth
- $P_{\max}$ -- attainable throughput under the roofline model

## Key Points

- Low arithmetic intensity usually means memory-bound behavior.
- High arithmetic intensity can still be memory-bound if bandwidth is weak.
- Roofline is a first-order model, not a perfect profiler.

## Function

```python
def roofline(
    flops: float,
    bytes_moved: float,
    peak_flops_per_s: float,
    memory_bandwidth_bytes_per_s: float,
) -> tuple[float, float, str]:
```

## Run tests

```bash
pytest modules/ml/systems/roofline-analysis/python -q
```
