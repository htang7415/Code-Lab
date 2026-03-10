# Global Average Pooling

> Track: `ml` | Topic: `computer-vision`

## Concept

Global average pooling replaces a spatial feature map with one mean value per
channel. It is a lightweight way to build a classifier head without flattening
the whole map.

## Math

$$y = \frac{1}{HW}\sum_{i=1}^{H}\sum_{j=1}^{W} x_{ij}$$

- $H, W$ -- feature-map height and width
- $x_{ij}$ -- activation at spatial location $(i, j)$
- $y$ -- pooled output

## Function

```python
def global_average_pool(feature_map: list[list[float]]) -> float:
```

## Run tests

```bash
pytest modules/ml/computer-vision/global-average-pooling/python -q
```
