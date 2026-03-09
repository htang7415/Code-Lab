# Backpropagation

> Track: `ml` | Topic: `deep-learning`

## Concept

Backpropagation computes parameter gradients by repeatedly applying the chain
rule from the loss back through each operation. For a linear unit, it answers:
"if the output loss changes by this much, how much did the weight contribute?"

## Math
$$\frac{\partial L}{\partial w} = \frac{\partial L}{\partial z} \cdot x$$

- $L$ -- loss
- $w$ -- weight
- $z = wx + b$ -- linear pre-activation
- $\frac{\partial L}{\partial z}$ -- upstream gradient arriving from later layers
- $x$ -- input value
- $\frac{\partial L}{\partial w}$ -- gradient of the loss with respect to the weight

## Key Points

- Gradients flow backward, but each local derivative is simple.
- For a linear unit, the weight gradient is just input times upstream gradient.
- Backprop is efficient because it reuses intermediate values from the forward pass.

## Function

```python
def linear_backprop(x: float, w: float, grad_out: float) -> float:
```

## Run tests

```bash
pytest modules/ml/deep-learning/backpropagation/python -q
```
