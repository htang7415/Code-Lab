# Supervised Fine-Tuning

> Track: `ml` | Topic: `llm`

## Concept

SFT trains on curated prompt-response pairs with teacher forcing.

## Math

$$\mathcal{L} = -\frac{1}{\sum_i m_i} \sum_i m_i \log p_\theta(y_i \mid x_i)$$

- $\mathcal{L}$ -- masked cross-entropy loss
- $m_i$ -- mask for supervised tokens (1 if included)
- $y_i$ -- target token at position $i$
- $p_\theta(y_i \mid x_i)$ -- model probability of the target token

- $\theta$ -- model parameters
- $x_i$ -- i-th input (feature vector or sample)
- $i$ -- index
- $m$ -- number of features/units
- $p$ -- probability
- $y$ -- target/label
- $x$ -- input (feature vector or sample)

## Function

```python
def sft_loss(logits: list[list[float]], targets: list[int], mask: list[int]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/supervised-fine-tuning/python -q
```
