# ResNet

> Track: `ml` | Topic: `computer-vision`

## Concept

ResNet is a classic CNN architecture with characteristic layer design.

## Math
$$x_{l+1} = x_l + F(x_l)$$

- $x_l$ -- input (feature vector or sample) for l
- $x$ -- input (feature vector or sample)

## Function

```python
def layers() -> list[str]:
```

## Run tests

```bash
pytest modules/ml/computer-vision/resnet/python -q
```