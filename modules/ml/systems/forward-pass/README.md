# Forward Pass

> Track: `ml` | Topic: `systems`

## Concept

The forward pass computes the model's output by propagating input data through each layer sequentially, from the first hidden layer to the final prediction. At every layer, a linear transformation is applied followed by a non-linear activation function. The composition of these transformations gives the network its expressive power.

During training, the forward pass also records all intermediate activations in the computational graph so that the backward pass can compute gradients. During inference, this bookkeeping is unnecessary and can be disabled (e.g., `torch.no_grad()`) to save memory and improve throughput. Understanding the forward pass is essential because the structure of the computation determines both the model's capacity and the shape of gradients that flow backward.

## Math

For a single layer with weight matrix $W$, bias vector $b$, and activation function $\sigma$:

$$h = \sigma(W x + b)$$

For a network with $N$ layers, the full forward pass composes each layer:

$$h^{(l)} = \sigma^{(l)}\!\left(W^{(l)} h^{(l-1)} + b^{(l)}\right), \quad l = 1, \dots, N$$

- $x$ -- input feature vector (or $h^{(0)}$)
- $W^{(l)}$ -- weight matrix at layer $l$
- $b^{(l)}$ -- bias vector at layer $l$
- $\sigma^{(l)}$ -- activation function at layer $l$ (e.g., ReLU, sigmoid)
- $h^{(l)}$ -- hidden representation (activation) at layer $l$

## Key Points

- Intermediate activations must be stored during training for use in the backward pass, which is why training consumes more memory than inference.
- In inference mode, gradient tracking is disabled to reduce memory usage and computation.
- The choice of activation function at each layer affects both the forward output and the gradient behavior during backpropagation.
- Batch dimensions are handled implicitly: $x$ is typically a matrix where each row is one sample in the mini-batch.

## Function

```python
def forward(x: list[float], w: list[float], b: float) -> float:
```

- `x` -- input feature vector
- `w` -- weight vector (one weight per input feature)
- `b` -- scalar bias term

## Run tests

```bash
pytest modules/ml/systems/forward-pass/python -q
```
