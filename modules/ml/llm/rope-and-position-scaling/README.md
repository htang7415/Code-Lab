# RoPE and Position Scaling

> Track: `ml` | Topic: `llm`

## Purpose

Use this module to understand how rotary position embedding encodes position
inside attention and how simple position scaling extends context length.

## First Principles

- RoPE rotates each even-odd feature pair by a position-dependent angle.
- Relative position information comes from phase differences, not from adding a
  separate position vector to the token embedding.
- Context extension often rescales positions before applying RoPE so new
  positions stay closer to the range seen during training.
- Position scaling helps long context, but aggressive scaling can distort
  short-context behavior.

## Core Math

RoPE pair frequency:

$$
\theta_i = \mathrm{base}^{-2i / d_{\text{model}}}
$$

RoPE rotation angle:

$$
\phi(p, i) = p \cdot \theta_i
$$

Linear position scaling for context extension:

$$
p' = p \cdot \frac{L_{\text{train}}}{L_{\text{target}}}
$$

- $i$ -- feature-pair index
- $p$ -- token position
- $d_{\text{model}}$ -- hidden width
- $L_{\text{train}}$ -- original training context length
- $L_{\text{target}}$ -- new target context length

## From Math To Code

- Compute the per-pair RoPE frequency first.
- Multiply position by that frequency to get the raw rotation angle.
- Rescale positions before angle computation when extending context.
- Keep the scaling rule simple before comparing more advanced extension methods.

## Minimal Code Mental Model

```python
freq = rope_pair_frequency(pair_index=1, d_model=8)
angle = rope_rotation_angle(position=128, pair_index=1, d_model=8)
scaled_pos = linear_scaled_position(position=8192, original_context=4096, target_context=8192)
scaled_angle = rope_scaled_angle(
    position=8192,
    pair_index=1,
    d_model=8,
    original_context=4096,
    target_context=8192,
)
```

## Function

```python
def rope_pair_frequency(pair_index: int, d_model: int, base: float = 10000.0) -> float:
def rope_rotation_angle(
    position: float,
    pair_index: int,
    d_model: int,
    base: float = 10000.0,
) -> float:
def linear_scaled_position(position: int, original_context: int, target_context: int) -> float:
def rope_scaled_angle(
    position: int,
    pair_index: int,
    d_model: int,
    original_context: int,
    target_context: int,
    base: float = 10000.0,
) -> float:
```

## When To Use What

- Use `rope_pair_frequency` and `rope_rotation_angle` to understand base RoPE.
- Use `linear_scaled_position` when the main question is simple context-window extension.
- Use `rope_scaled_angle` when you want to see how scaling changes the actual phase used by attention.

## References

- Su et al. (2021). [RoFormer: Enhanced Transformer with Rotary Position Embedding](https://arxiv.org/abs/2104.09864)
- Peng et al. (2023). [YaRN: Efficient Context Window Extension of Large Language Models](https://arxiv.org/abs/2309.00071)
- Ding et al. (2024). [LongRoPE: Extending LLM Context Window Beyond 2 Million Tokens](https://www.microsoft.com/en-us/research/publication/longrope-extending-llm-context-window-beyond-2-million-tokens/)

## Run tests

```bash
pytest modules/ml/llm/rope-and-position-scaling/python -q
```
