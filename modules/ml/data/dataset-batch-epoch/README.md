# Dataset vs Batch vs Epoch

> Track: `ml` | Topic: `data`

## Concept

A dataset is the full collection of samples available for training. A batch (or mini-batch) is a subset of the dataset used in a single parameter update step. An epoch is one complete pass through the entire dataset. These three concepts define the rhythm of training: within each epoch the data is divided into batches, and the model parameters are updated once per batch.

The choice of batch size $B$ is a key hyperparameter that affects both optimization dynamics and hardware utilization. Smaller batches inject noise into gradient estimates, which can act as implicit regularization and help escape sharp minima. Larger batches give more accurate gradients and better GPU throughput, but training for too many epochs risks overfitting as the model begins to memorize the training data rather than learning general patterns.

## Math
$$\text{updates/epoch} = \left\lceil \frac{N}{B} \right\rceil,\quad \text{total updates} = E \left\lceil \frac{N}{B} \right\rceil$$

- $N$ -- number of samples in the dataset
- $B$ -- batch size
- $E$ -- number of epochs

## Key Points

- More epochs allow the model to see every sample multiple times, but too many epochs risk overfitting.
- Batch size is a critical hyperparameter: it controls the trade-off between gradient noise and computational efficiency.
- One training step (weight update) corresponds to one batch, not one epoch.
- Common batch sizes are powers of two (32, 64, 128, 256) to align with GPU memory architecture.

## Function

```python
def num_batches(dataset_size: int, batch_size: int) -> int:
```

- `dataset_size` -- total number of samples in the dataset ($N$)
- `batch_size` -- number of samples per batch ($B$)

## Run tests

```bash
pytest modules/ml/data/dataset-batch-epoch/python -q
```
