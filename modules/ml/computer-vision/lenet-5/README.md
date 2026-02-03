# LeNet-5

> Track: `ml` | Topic: `computer-vision`

## Concept

LeNet-5 is a classic CNN architecture with characteristic layer design.

## Math
$$f(x) = f_L \circ f_{L-1} \circ \cdots \circ f_1(x)$$

- $x$ -- input (feature vector or sample)
- $L$ -- loss value

## Function

```python
def layers() -> list[str]:
```

## Run tests

```bash
pytest modules/ml/computer-vision/lenet-5/python -q
```