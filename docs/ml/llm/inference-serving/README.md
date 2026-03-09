# LLM Inference Serving

Serving quality depends on latency, memory, batching, and hardware efficiency more than on model architecture alone.

## Current Anchors

- KV cache sizing (`modules/ml/llm/kv-cache`)
- Prefix-cache reuse (`modules/ml/llm/prefix-cache`)
- Speculative decoding verification (`modules/ml/llm/speculative-decoding`)
- Inference head pruning (`modules/ml/llm/inference-head-pruning`)
- INT8 / INT4 quantization (`modules/ml/llm/int8-int4-quantization`)
- FP16 / BF16 / FP8 trade-offs (`modules/ml/llm/fp16-bf16-fp8`)
- Request batching (`modules/ml/mlops/request-batching`)
- Continuous batching (`modules/ml/systems/continuous-batching`)
- Roofline analysis (`modules/ml/systems/roofline-analysis`)

## Concepts to Cover Well

- TTFT, ITL, and tokens/sec
- Continuous batching and chunked prefill
- KV cache memory budgets and eviction
- Prefix cache reuse
- Speculative decoding and verification
