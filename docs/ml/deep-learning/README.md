# Foundations of Deep Learning

Neural networks and training mechanics from first principles.
Each bullet maps to a module under `modules/ml/deep-learning/` unless noted.

## Neural Networks and Backprop

- Feedforward neural networks (`modules/ml/deep-learning/feedforward-neural-network`)
- Neuron, weights, bias, activation (`modules/ml/deep-learning/neuron-weights-bias-activation`)
- Backpropagation (chain rule, local gradients) (`modules/ml/deep-learning/backpropagation`)
- Automatic differentiation (forward vs backward mode) (`modules/ml/deep-learning/automatic-differentiation`)
- Vanishing and exploding gradients (`modules/ml/deep-learning/vanishing-exploding-gradients`)
- Gradient checking (finite differences) (`modules/ml/deep-learning/gradient-checking`)

## Activation Functions

- Sigmoid, Tanh, Hard Sigmoid, Dynamic Tanh, Hardtanh (`modules/ml/deep-learning/activations-sigmoid-tanh`)
- ReLU family: ReLU, Leaky ReLU, ELU, PReLU (`modules/ml/deep-learning/activations-relu-family`)
- Modern: GeLU, Swish, SwiGLU, Mish (`modules/ml/deep-learning/activations-modern`)
- Softmax, Softplus, Softsign (`modules/ml/deep-learning/activations-softmax-softplus-softsign`)
- Failure modes (dead ReLU, saturation) (`modules/ml/deep-learning/activation-failure-modes`)

## Initialization

- Xavier / Glorot: symmetric activations (`modules/ml/deep-learning/xavier-initialization`)
- He initialization: ReLU (`modules/ml/deep-learning/he-initialization`)
- Effect on gradient flow (`modules/ml/deep-learning/gradient-flow`)

## Regularization

- L1 (Lasso) (`modules/ml/deep-learning/l1-regularization`)
- L2 (Ridge) (`modules/ml/deep-learning/l2-regularization`)
- Weight decay (`modules/ml/deep-learning/weight-decay`)
- Dropout (`modules/ml/deep-learning/dropout`)
- Early stopping (`modules/ml/deep-learning/early-stopping`)
- LoRA (conceptual regularization effect; see `modules/ml/llm/lora`)

## Loss Functions

### Classification

- Cross-entropy (`modules/ml/deep-learning/cross-entropy`)
- Hinge loss (`modules/ml/deep-learning/hinge-loss`)
- Focal loss (imbalanced data) (`modules/ml/deep-learning/focal-loss`)

### Regression

- MSE (`modules/ml/deep-learning/mse-loss`)
- MAE (`modules/ml/deep-learning/mae-loss`)
- RMSE (`modules/ml/deep-learning/rmse-loss`)
- Huber loss (`modules/ml/deep-learning/huber-loss`)

### Special

- Knowledge distillation loss (`modules/ml/deep-learning/knowledge-distillation-loss`)
- KL divergence (see `modules/ml/fundamentals/kl-divergence`)

## Normalization

- BatchNorm (train vs eval behavior) (`modules/ml/deep-learning/batchnorm`)
- LayerNorm (`modules/ml/deep-learning/layernorm`)
- RMSNorm (`modules/ml/deep-learning/rmsnorm`)
- GroupNorm (`modules/ml/deep-learning/groupnorm`)
- InstanceNorm (`modules/ml/deep-learning/instancenorm`)
- Why BatchNorm is bad for Transformers (`modules/ml/deep-learning/batchnorm-transformers`)
