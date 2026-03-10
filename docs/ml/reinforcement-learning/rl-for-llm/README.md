# RL for LLMs

RL for LLMs is mostly about preference optimization under expensive on-policy sampling and fragile reward signals.

## Current Anchors

- DPO vs PPO (`modules/ml/reinforcement-learning/dpo-vs-ppo`)
- Group-based optimization (`modules/ml/reinforcement-learning/group-based-optimization`)
- Reward clipping (`modules/ml/reinforcement-learning/reward-clipping`)
- Reward scale (`modules/ml/reinforcement-learning/reward-scale`)
- KL regularization (`modules/ml/llm/kl-regularization`)
- RLHF (`modules/ml/llm/rlhf`)

## Concepts to Cover Well

- Reward modeling and preference data
- PPO-style token-level ratio control
- GRPO / GSPO sequence-group objectives
- KL anchoring against base-model drift
- Credit assignment under long generated sequences
- Overoptimization, reward hacking, and judge mismatch
