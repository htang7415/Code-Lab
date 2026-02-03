# Batch Iterator

> Track: `ml` | Topic: `data`

## Concept

Mini-batch iteration is the process of shuffling a dataset and yielding fixed-size chunks of indices so that each chunk can be used as one gradient-update step. Stochastic gradient descent (SGD) relies on random mini-batches rather than the full dataset because smaller, randomized subsets reduce per-step computation while still providing an unbiased estimate of the true gradient.

Shuffling the data before each epoch ensures the model does not see examples in the same order repeatedly, which could introduce ordering bias and cause the optimizer to cycle through a fixed trajectory. After shuffling, the iterator slices the index sequence into consecutive blocks of size $B$, where the last block may contain fewer than $B$ elements if $N$ is not evenly divisible by $B$.

## Math
$$n_{\text{batches}} = \left\lceil \frac{N}{B} \right\rceil$$

$$b_i = [iB,\min((i+1)B,N))$$

- $n_{\text{batches}}$ -- number of batches
- $N$ -- number of samples in the dataset
- $B$ -- batch size
- $b_i$ -- index range for batch $i$
- $i$ -- batch index

## Key Points

- The last batch may be smaller than $B$ when $N$ is not divisible by $B$.
- Shuffling before each epoch prevents ordering bias and improves convergence.
- Batch size directly affects gradient variance: smaller batches give noisier but more frequent updates, larger batches give smoother but fewer updates.
- Setting $B = 1$ recovers pure SGD; setting $B = N$ recovers full-batch gradient descent.

## Function

```python
def batch_indices(n: int, batch_size: int) -> list[list[int]]:
```

- `n` -- total number of samples in the dataset
- `batch_size` -- number of samples in each mini-batch

## Run tests

```bash
pytest modules/ml/data/batch-iterator/python -q
```
