# GPU Performance

GPU reasoning should connect model math to memory traffic and achievable throughput.

## Current Anchors

- Mixed precision training (`modules/ml/systems/mixed-precision`)
- FP16 / BF16 / FP8 trade-offs (`modules/ml/llm/fp16-bf16-fp8`)
- INT8 / INT4 quantization (`modules/ml/llm/int8-int4-quantization`)
- Roofline analysis (`modules/ml/systems/roofline-analysis`)

## Concepts to Cover Well

- Arithmetic intensity
- Compute-bound vs memory-bound kernels
- Quantization and memory savings
- Kernel fusion and bandwidth pressure
