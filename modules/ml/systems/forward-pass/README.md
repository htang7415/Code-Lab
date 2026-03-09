# Forward Pass

> Track: `ml` | Topic: `systems`

## Concept

The forward pass applies the model's current parameters to an input and produces
an output. This lab isolates the smallest useful piece of that process: one
affine step, or one neuron's pre-activation.

In a full network, many such steps are chained together, often with
non-linearities between them. During training, the forward pass also stores
intermediate values so the backward pass can later compute gradients.

## Math

For this minimal affine forward step:

$$z = w^\top x + b$$

If you then apply an activation $\sigma$, you get a neuron's output:

$$h = \sigma(z)$$

- $x$ -- input feature vector
- $w$ -- weight vector
- $b$ -- bias term
- $z$ -- pre-activation value
- $h$ -- activated output
- $\sigma$ -- activation function such as ReLU or sigmoid

## Key Points

- A forward pass always means "compute outputs from inputs using current
  parameters."
- This function computes the affine part only; deeper networks stack many such
  operations.
- Training usually stores forward intermediates because backprop needs them.

## Function

```python
def forward(x: list[float], w: list[float], b: float) -> float:
```

- `x` -- input feature vector
- `w` -- weight vector (one weight per input feature)
- `b` -- scalar bias term added after the dot product

## Run tests

```bash
pytest modules/ml/systems/forward-pass/python -q
```
