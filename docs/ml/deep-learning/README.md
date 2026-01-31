# Foundations of Deep Learning

Neural networks and training mechanics from first principles.

## Neural Networks and Backprop

- Feedforward neural networks
- Neuron, weights, bias, activation
- Backpropagation (chain rule, local gradients)
- Automatic differentiation (forward vs backward mode)
- Vanishing and exploding gradients
- Gradient checking (finite differences)

## Activation Functions

- Sigmoid, Tanh, Hard Sigmoid, Dynamic Tanh, Hardtanh
- ReLU family: ReLU, Leaky ReLU, ELU, PReLU
- Modern: GeLU, Swish, SwiGLU, Mish
- Softmax, Softplus, Softsign
- Failure modes (dead ReLU, saturation)

## Initialization

- Xavier / Glorot: symmetric activations
- He initialization: ReLU
- Effect on gradient flow

## Regularization

- L1 (Lasso)
- L2 (Ridge)
- Weight decay
- Dropout
- Early stopping
- LoRA (conceptual regularization effect)

## Loss Functions

### Classification

- Cross-entropy
- Hinge loss
- Focal loss (imbalanced data)

### Regression

- MSE
- MAE
- RMSE
- Huber loss

### Special

- Knowledge distillation loss
- KL divergence

## Normalization

- BatchNorm (train vs eval behavior)
- LayerNorm
- RMSNorm
- GroupNorm
- InstanceNorm
- Why BatchNorm is bad for Transformers
