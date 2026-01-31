# Diffusion Sampling and Guidance Trade-offs

> Track: `ml` | Topic: `generative`

## Concept

Classifier-free guidance is a technique that steers diffusion model sampling toward a conditioning signal (e.g., a text prompt) by amplifying the difference between the conditional and unconditional noise predictions. During training, the model learns both a conditional prediction $\epsilon_\theta(x_t, c)$ and an unconditional prediction $\epsilon_\theta(x_t)$ by randomly dropping the condition $c$. At inference, the two predictions are combined with a guidance scale $w$ that controls how strongly the condition influences generation.

The guidance scale creates a fundamental trade-off between fidelity and diversity. When $w = 0$, sampling is fully unconditional and produces maximum diversity but ignores the prompt. As $w$ increases, samples align more closely with the condition -- colors become more vivid, objects more recognizable -- but the distribution narrows and diversity drops. Very high guidance values produce oversaturated, artifact-prone images.

This trade-off mirrors the precision-recall trade-off in classification. Higher guidance improves precision (samples that match the condition) at the cost of recall (coverage of the full conditional distribution). In practice, $w$ between 3 and 15 is typical, and the optimal value depends on the application. Creative tasks favor lower guidance for variety, while tasks requiring exact prompt adherence favor higher guidance.

## Math

The guided noise prediction combines conditional and unconditional estimates:

$$\tilde{\epsilon} = (1 + w)\,\epsilon_\theta(x_t, c) - w\,\epsilon_\theta(x_t)$$

This is equivalent to extrapolating away from the unconditional prediction:

$$\tilde{\epsilon} = \epsilon_\theta(x_t) + (1 + w)\bigl(\epsilon_\theta(x_t, c) - \epsilon_\theta(x_t)\bigr)$$

- $w$ -- guidance scale (0 = unconditional, higher = stronger conditioning)
- $\epsilon_\theta(x_t, c)$ -- noise prediction conditioned on $c$
- $\epsilon_\theta(x_t)$ -- unconditional noise prediction (condition dropped)
- $c$ -- conditioning signal (e.g., text embedding, class label)

## Key Points

- At $w = 0$ the model samples unconditionally; increasing $w$ trades diversity for stronger adherence to the conditioning signal.
- Typical guidance scales are $w \in [3, 15]$; values beyond this range tend to produce oversaturated images with artifacts.
- Classifier-free guidance requires no external classifier -- the model is trained to handle both conditional and unconditional denoising by randomly dropping the condition.
- The fidelity-diversity trade-off from guidance is analogous to the temperature parameter in language models: higher guidance concentrates the output distribution.
- Guidance can be applied per-step, and dynamic schedules (e.g., higher guidance early, lower late) can improve results.

## Function

```python
def guided_step(base: float, cond: float, scale: float) -> float:
```

- `base` -- unconditional noise prediction $\epsilon_\theta(x_t)$
- `cond` -- conditional noise prediction $\epsilon_\theta(x_t, c)$
- `scale` -- guidance scale $w$

## Run tests

```bash
pytest modules/ml/generative/diffusion-guidance-tradeoffs/python -q
```
