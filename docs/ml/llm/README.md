# NLP and LLMs

Transformers, training stages, and alignment for LLMs.
Each bullet maps to a module under `modules/ml/llm/`.

## Core Concepts

- Tokenization (`modules/ml/llm/tokenization`)
- Embeddings (`modules/ml/llm/embeddings`)
- Positional encoding (`modules/ml/llm/positional-encoding`)
- Transformer (`modules/ml/llm/transformer`)
- Self-attention (`modules/ml/llm/self-attention`)
- Multi-head attention (`modules/ml/llm/multi-head-attention`)
- Masked attention (`modules/ml/llm/attention-causal`)

## Training Stages

- Pretraining (next-token prediction / PTX loss) (`modules/ml/llm/pretraining`)
- Supervised fine-tuning (SFT) (`modules/ml/llm/supervised-fine-tuning`)
- Alignment / preference learning (`modules/ml/llm/preference-learning`)

## Alignment and Optimization

- RLHF (`modules/ml/llm/rlhf`)
- DPO (`modules/ml/llm/dpo`)
- KL regularization (`modules/ml/llm/kl-regularization`)
- PTX anchoring (`modules/ml/llm/ptx-anchoring`)

## Efficiency and Systems

- LoRA (`modules/ml/llm/lora`) / QLoRA (`modules/ml/llm/qlora`)
- Inference head pruning (`modules/ml/llm/inference-head-pruning`)
- Sparse attention (`modules/ml/llm/sparse-attention`)
- MoE (Top-K routing, Noisy gating) (`modules/ml/llm/moe-routing`)
- FP16 / BF16 / FP8 (`modules/ml/llm/fp16-bf16-fp8`)
- INT8 / INT4 (`modules/ml/llm/int8-int4-quantization`)
