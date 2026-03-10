# Transition Indicators and Masks

Transition indicators turn episode termination state into tensors that control bootstrapping and loss masking.

## Metric Families

- Binary masks: terminal mask, continuation mask, not-done mask
- Fraction summaries: done fraction, nonterminal fraction, terminal share
- Per-transition indicators: terminal indicator, nonterminal indicator, continuing indicator
- Batch helpers: done indicator batch, continuing transition batch, resilient transition batch

## How to Use Them

- Use binary masks when computing TD targets or bootstrapped returns.
- Use fraction summaries for dataset-level diagnostics.
- Use per-transition indicators when the pipeline expects numeric features instead of booleans.
- Use batch helpers when shaping tensors for vectorized RL code.

## Good Defaults

- `terminal-mask` for TD target logic
- `done-fraction` or `episode-end-rate` for replay-buffer diagnostics
- `bootstrap-target` plus `terminal-mask` as the core teaching pair
