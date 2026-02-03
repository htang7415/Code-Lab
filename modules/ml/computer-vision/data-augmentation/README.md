# Data Augmentation

> Track: `ml` | Topic: `computer-vision`

## Concept

Augmentation applies random transforms like flips.

## Math
$$x' = \mathrm{flip}(x)$$

- $x$ -- input (feature vector or sample)

## Function

```python
def horizontal_flip(image: list[list[int]]) -> list[list[int]]:
```

## Run tests

```bash
pytest modules/ml/computer-vision/data-augmentation/python -q
```