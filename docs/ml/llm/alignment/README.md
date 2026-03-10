# LLM Alignment

Alignment is the stack that turns a capable next-token model into one that follows instructions and preferences.

## Current Anchors

- Supervised fine-tuning (`modules/ml/llm/supervised-fine-tuning`)
- Preference learning (`modules/ml/llm/preference-learning`)
- RLHF (`modules/ml/llm/rlhf`)
- DPO (`modules/ml/llm/dpo`)
- KL regularization (`modules/ml/llm/kl-regularization`)
- PTX anchoring (`modules/ml/llm/ptx-anchoring`)
- Group-based optimization (`modules/ml/reinforcement-learning/group-based-optimization`)

## Concepts to Cover Well

- SFT as the first alignment stage
- Reward-model-driven RLHF vs direct preference objectives
- KL control as a guardrail against policy drift
- PTX anchoring to preserve base capabilities
- GRPO / GSPO as lower-memory alternatives to PPO-style alignment
- Judge-based evaluation and reward hacking failure modes
