# Supervised Fine-Tuning

> Track: `ml` | Topic: `llm`

## Concept

Supervised fine-tuning (SFT) trains a language model on curated prompt-response
pairs. Teacher forcing means the model is always conditioned on the correct
previous tokens while learning to predict the next target token.

## Math

$$\mathcal{L} = -\frac{1}{\sum_i m_i} \sum_i m_i \log p_\theta(y_i \mid x_i)$$

- $\mathcal{L}$ -- masked cross-entropy loss
- $m_i$ -- mask for supervised tokens (1 if token $i$ should contribute)
- $y_i$ -- target token at position $i$
- $x_i$ -- conditioning context used to predict token $y_i$
- $p_\theta(y_i \mid x_i)$ -- model probability assigned to the target token
- $\theta$ -- model parameters
- $i$ -- index

## Key Points

- The mask excludes prompt tokens or padding positions from the loss.
- SFT teaches imitation of the reference completion, not exploration.
- This is usually the stage between pretraining and preference alignment.

## Function

```python
def sft_loss(logits: list[list[float]], targets: list[int], mask: list[int]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/supervised-fine-tuning/python -q
```
