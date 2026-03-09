# BLEU and METEOR Overlap

> Track: `ml` | Topic: `llm`

## Concept

BLEU and METEOR are classic text-generation metrics based on token overlap with a reference.
This module uses a compact BLEU-1 and METEOR-style unigram matching baseline.

## Math

$$\mathrm{BLEU}\text{-}1 = \mathrm{BP} \cdot \frac{m}{c}$$

$$\mathrm{METEOR} = \frac{10PR}{R + 9P}$$

- $m$ -- matched unigram count
- $c$ -- candidate token count
- $P$ -- unigram precision
- $R$ -- unigram recall
- $\mathrm{BP}$ -- brevity penalty

## Key Points

- BLEU emphasizes precision and penalizes very short candidates.
- METEOR mixes precision and recall more directly.
- Modern LLM evaluation often uses stronger task-specific metrics, but these still appear in problem banks.

## Function

```python
def bleu1_meteor(
    candidate: str,
    reference: str,
) -> tuple[float, float]:
```

## Run tests

```bash
pytest modules/ml/llm/bleu-meteor/python -q
```
