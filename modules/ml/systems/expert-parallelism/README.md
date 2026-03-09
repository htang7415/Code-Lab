# Expert Parallel Dispatch

> Track: `ml` | Topic: `systems`

## Concept

Expert parallelism places different experts on different shards.
When a router sends a token to an expert on another shard, the token must be dispatched across the network.

## Math

$$s(e) = \left\lfloor \frac{e}{E_{\mathrm{per\_shard}}} \right\rfloor$$

$$D_{\mathrm{remote}} = \sum_i \mathbb{I}[h_i \ne s(e_i)]$$

- $e_i$ -- expert assigned to token $i$
- $h_i$ -- home shard for token $i$
- $s(e_i)$ -- shard that owns expert $e_i$
- $E_{\mathrm{per\_shard}}$ -- number of experts stored on one shard
- $D_{\mathrm{remote}}$ -- number of tokens that must be dispatched remotely

## Key Points

- Expert parallelism scales MoE capacity without keeping every expert on every device.
- Routing quality and communication cost are tied together.
- This module tracks token dispatch counts, not expert compute time or load-balancing losses.

## Function

```python
def expert_parallel_dispatch_stats(
    token_home_shards: list[int],
    expert_assignments: list[int],
    experts_per_shard: int,
) -> tuple[list[int], int]:
```

## Run tests

```bash
pytest modules/ml/systems/expert-parallelism/python -q
```
