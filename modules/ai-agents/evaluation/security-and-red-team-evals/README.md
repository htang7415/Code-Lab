# Security and Red-Team Evals

> Track: `ai-agents` | Topic: `evaluation`

## Concept

Security and red-team evals measure whether an agent resists attacks such as prompt injection, data exfiltration, privilege escalation, and unsafe action requests before a release.

## Key Points

- Security evals are attack-focused, not just general quality benchmarks.
- High-risk attack failures should count more heavily than ordinary misses.
- A release gate should combine overall pass rate with a separate check for high-risk failures.

## Minimal Code Mental Model

```python
breakdown = security_eval_breakdown(["prompt_injection", "unsafe_action", "prompt_injection"])
high_risk = high_risk_failure_count(breakdown)
route = security_release_gate(pass_rate=0.94, high_risk_failures=high_risk, min_pass_rate=0.9)
```

## Function

```python
def security_eval_breakdown(failed_attack_types: list[str]) -> dict[str, int]:
def high_risk_failure_count(
    breakdown: dict[str, int],
    high_risk_labels: list[str] | None = None,
) -> int:
def security_release_gate(pass_rate: float, high_risk_failures: int, min_pass_rate: float) -> str:
```

## References

- Perez et al. (2022). [Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors, and Lessons Learned](https://arxiv.org/abs/2209.07858)
- Greshake et al. (2023). [Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/abs/2302.12173)
- Yi et al. (2023). [Benchmarking and Defending Against Indirect Prompt Injection Attacks on Large Language Models](https://arxiv.org/abs/2312.14197)

## Run tests

```bash
pytest modules/ai-agents/evaluation/security-and-red-team-evals/python -q
```
