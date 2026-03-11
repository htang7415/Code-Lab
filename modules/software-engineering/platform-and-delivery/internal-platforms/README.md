# Internal Platforms

> Track: `software-engineering` | Topic: `platform-and-delivery`

## Concept

An internal platform is justified when many teams repeat the same infrastructure or delivery work and a shared abstraction can remove that toil without hiding essential choices.

## Key Points

- A platform should solve repeated pain, not invent new surfaces to maintain.
- Too many exceptions are a sign the abstraction is premature or too broad.
- Platform value depends on adoption and reduced repeated work.

## Minimal Code Mental Model

```python
worth_it = platform_candidate(teams=6, repeated_work_hours_per_team=5, custom_exceptions=1)
risk = abstraction_risk(custom_exceptions=5)
value = platform_value(teams=6, repeated_work_hours_per_team=5)
```

## Function

```python
def platform_candidate(teams: int, repeated_work_hours_per_team: int, custom_exceptions: int) -> bool:
def abstraction_risk(custom_exceptions: int) -> str:
def platform_value(teams: int, repeated_work_hours_per_team: int) -> int:
```

## Run tests

```bash
pytest modules/software-engineering/platform-and-delivery/internal-platforms/python -q
```
