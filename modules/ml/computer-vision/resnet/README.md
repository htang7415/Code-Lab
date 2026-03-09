# ResNet

> Track: `ml` | Topic: `computer-vision`

## Concept

ResNet is a family of CNNs built around residual blocks. Instead of learning an
entire transformation from scratch, each block learns a residual update
$F(x_l)$, which is added back to the shortcut signal $x_l$.

## Math
$$x_{l+1} = x_l + F(x_l)$$

- $x_l$ -- input activation to residual block $l$
- $F(x_l)$ -- learned residual transformation
- $x_{l+1}$ -- output activation after the skip connection

## Key Points

- Skip connections make optimization easier by preserving a direct gradient path.
- A full ResNet stacks multiple residual stages after an initial convolutional
  stem.
- This lab returns a high-level stage layout, not a full CNN implementation.

## Function

```python
def layers() -> list[str]:
```

## Run tests

```bash
pytest modules/ml/computer-vision/resnet/python -q
```
