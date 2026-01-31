# CNNs

> Track: `ml` | Topic: `computer-vision`

## Concept

CNNs use convolutional filters to capture local patterns.

## Math

$$feature_map = conv(input, kernel)$$

## Function

```python
def conv1d(signal: list[float], kernel: list[float]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/computer-vision/cnn-basics/python -q
```
