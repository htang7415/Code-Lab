# Training Loop Mechanics

Training loop mechanics and debugging signals.
Each bullet maps to a module under `modules/ml/systems/`.

## Core Steps

- Zeroing gradients (`modules/ml/systems/zero-gradients`)
- Forward pass (`modules/ml/systems/forward-pass`)
- Backward pass (`modules/ml/systems/backward-pass`)
- Optimizer step (`modules/ml/systems/optimizer-step`)
- Gradient accumulation (`modules/ml/systems/gradient-accumulation`)
- Mixed precision training (`modules/ml/systems/mixed-precision`)
- Check gradients are flowing (`modules/ml/systems/check-gradients`)
- Debug overfitting vs underfitting (`modules/ml/systems/debug-overfit-underfit`)
