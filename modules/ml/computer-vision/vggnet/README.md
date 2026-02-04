# VGGNet

> Track: `ml` | Topic: `computer-vision`

## Concept

VGGNet stacks many small 3×3 convolutions with max-pooling for depth and simplicity.

## Math
Two 3×3 convolutions approximate a single 5×5 receptive field.

## Function

```python
def layers() -> list[str]:
```

## Run tests

```bash
pytest modules/ml/computer-vision/vggnet/python -q
```
