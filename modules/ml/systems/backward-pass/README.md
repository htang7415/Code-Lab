# Backward Pass

> Track: `ml` | Topic: `systems`

## Concept

The backward pass computes the gradient of the loss function with respect to every learnable parameter in the network. Starting from the scalar loss at the output, it applies the chain rule layer by layer in reverse order, propagating error signals back through the computational graph. This process is the core of backpropagation and is what makes gradient-based optimization possible.

Each node in the computational graph stores intermediate activations from the forward pass so that partial derivatives can be computed locally. The chain rule then multiplies these local gradients together along every path from the loss to a given parameter. Because modern frameworks build dynamic or static computation graphs automatically, the backward pass is typically invoked with a single call, but understanding its mechanics is essential for debugging vanishing or exploding gradients.

## Math

For a parameter $w$ in a layer that produces output $y$ contributing to loss $L$, the chain rule gives:

$$\frac{\partial L}{\partial w} = \frac{\partial L}{\partial y} \cdot \frac{\partial y}{\partial w}$$

For a multi-layer network with layers $l = 1, \dots, N$, the gradient flows recursively:

$$\frac{\partial L}{\partial h^{(l)}} = \frac{\partial L}{\partial h^{(l+1)}} \cdot \frac{\partial h^{(l+1)}}{\partial h^{(l)}}$$

- $L$ -- scalar loss value
- $w$ -- a learnable weight parameter
- $y$ -- layer output (activation)
- $h^{(l)}$ -- hidden representation at layer $l$

- $N$ -- number of samples
- $h$ -- hidden representation

## Key Points

- The backward pass must run after the forward pass because it relies on cached intermediate activations.
- The computation graph stores every operation and intermediate value, which is why training uses significantly more memory than inference.
- Vanishing gradients occur when many small derivatives are multiplied together; exploding gradients occur with large derivatives -- both are diagnosed by inspecting backward-pass outputs.
- Detaching a tensor from the graph stops gradient flow, which is useful for frozen layers or stop-gradient tricks.

## Function

```python
def backward(dy: float, x: float) -> float:
```

- `dy` -- upstream gradient $\frac{\partial L}{\partial y}$ flowing back from the next layer
- `x` -- input activation cached during the forward pass

## Run tests

```bash
pytest modules/ml/systems/backward-pass/python -q
```
