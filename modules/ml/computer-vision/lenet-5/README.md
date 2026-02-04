# LeNet-5

> Track: `ml` | Topic: `computer-vision`

## Concept

LeNet-5 is an early CNN for digit recognition with two conv+pool stages
followed by fully connected layers.

## Math
$$f(x) = f_L \circ f_{L-1} \circ \cdots \circ f_1(x)$$

- $x$ -- input image
- $L$ -- number of layers

## Function

```python
def layers() -> list[str]:
```

## Run tests

```bash
pytest modules/ml/computer-vision/lenet-5/python -q
```
