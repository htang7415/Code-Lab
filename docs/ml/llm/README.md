# NLP and LLMs

Transformers, training stages, and alignment for LLMs.
Each bullet maps to a module under `modules/ml/llm/`.

## Core Concepts

- Tokenization (`modules/ml/llm/tokenization`)
- Tokenizer comparison (`modules/ml/llm/tokenizer-comparison`)
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

## Evaluation

- LLM evaluation guide (`docs/ml/llm/evaluation`)
- Likelihood and task scoring: `perplexity`, `exact-match`, `answer-verification`, `pass-at-k`, `mmlu-evaluation`, `bleu-meteor`
- Consensus and sampling: `self-consistency-voting`, `answer-stability`, `candidate-diversity`, plus the vote metrics guide
- Judge and preference evaluation: `judge-calibration`, `judge-pairwise`, `judge-agreement-matrix`
- Retrieval and reranking: `retrieval-metrics`, `reranker-metrics`, `mean-reciprocal-rank`, `ndcg`

## Retrieval and Lexical Baselines

- BM25 ranking (`modules/ml/llm/bm25-ranking`)
- Weighted retrieval fusion (`modules/ml/llm/retrieval-fusion`)
- Reciprocal-rank fusion (`modules/ml/llm/reciprocal-rank-fusion`)

## Decoding

- Decoding methods family (`modules/ml/llm/decoding-methods`)
- Beam search (`modules/ml/llm/beam-search`)
- Top-k sampling (`modules/ml/llm/top-k-sampling`)
- Top-p sampling (`modules/ml/llm/top-p-sampling`)
- Temperature sampling (`modules/ml/llm/temperature-sampling`)
- Combined sampling pipeline (`modules/ml/llm/sampling-pipeline`)

## Alignment and Optimization

- RLHF (`modules/ml/llm/rlhf`)
- DPO (`modules/ml/llm/dpo`)
- KL regularization (`modules/ml/llm/kl-regularization`)
- PTX anchoring (`modules/ml/llm/ptx-anchoring`)

## Efficiency and Systems

- LoRA (`modules/ml/llm/lora`) / QLoRA (`modules/ml/llm/qlora`)
- KV cache sizing (`modules/ml/llm/kv-cache`)
- Prefix-cache reuse (`modules/ml/llm/prefix-cache`)
- Speculative decoding verification (`modules/ml/llm/speculative-decoding`)
- Inference head pruning (`modules/ml/llm/inference-head-pruning`)
- Sparse attention (`modules/ml/llm/sparse-attention`)
- QK-clip / MuonClip attention stabilization (`modules/ml/llm/qk-clip`)
- Sparse MoE layers (top-k expert routing) (`modules/ml/llm/moe-routing`)
- FP16 / BF16 / FP8 (`modules/ml/llm/fp16-bf16-fp8`)
- INT8 / INT4 (`modules/ml/llm/int8-int4-quantization`)

See also:

- Tokenization guide (`docs/ml/llm/tokenization`)
- Alignment guide (`docs/ml/llm/alignment`)
- LLM evaluation guide (`docs/ml/llm/evaluation`)
- Inference serving guide (`docs/ml/llm/inference-serving`)
