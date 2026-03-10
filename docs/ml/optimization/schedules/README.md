# Learning Rate Schedules

Schedules shape how aggressively optimization explores early and settles late.

## Current Anchors

- Constant LR (`modules/ml/optimization/lr-constant`)
- Step decay (`modules/ml/optimization/lr-step-decay`)
- Exponential decay (`modules/ml/optimization/lr-exponential-decay`)
- Warmup (`modules/ml/optimization/lr-warmup`)
- Cosine decay (`modules/ml/optimization/lr-cosine-decay`)
- Warmup plus cosine decay (`modules/ml/optimization/warmup-cosine-decay`)
- One-cycle schedule (`modules/ml/optimization/one-cycle-schedule`)
- Cosine restarts (`modules/ml/optimization/cosine-restarts`)

## Concepts to Cover Well

- Warmup to avoid early instability
- Monotone decay when late optimization should get conservative
- Cosine schedules for smooth annealing
- Restarts for periodic exploration
- One-cycle as an aggressive train-fast schedule
- Matching schedule shape to batch size, optimizer, and training length
