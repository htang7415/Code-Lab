# Deep Learning Training Techniques

Training techniques are the pragmatic layer between a correct model and a trainable one.

## Current Anchors

- Dropout (`modules/ml/deep-learning/dropout`)
- Early stopping (`modules/ml/deep-learning/early-stopping`)
- Weight decay (`modules/ml/deep-learning/weight-decay`)
- Knowledge distillation loss (`modules/ml/deep-learning/knowledge-distillation-loss`)
- Focal loss (`modules/ml/deep-learning/focal-loss`)
- Label smoothing (`modules/ml/deep-learning/label-smoothing`)
- Gradient clipping (`modules/ml/optimization/gradient-clipping`)
- Loss scaling (`modules/ml/optimization/loss-scaling`)

## Concepts to Cover Well

- Regularization that changes the model vs regularization that changes the targets
- Why distillation is about soft targets, not just copying a bigger model
- Label smoothing as confidence control for classification
- Focal loss for class imbalance and hard-example focus
- Early stopping and weight decay as low-complexity defaults
- Gradient clipping and loss scaling as numerical-stability tools
