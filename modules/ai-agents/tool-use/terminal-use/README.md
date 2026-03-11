# Terminal Use

> Track: `ai-agents` | Topic: `tool-use`

## Concept

Terminal use is tool use through a shell, where the agent must classify command risk, prefer structured output, and stop for review before destructive actions.

## Key Points

- Shell tools can inspect, transform, or delete real state, so command risk matters before execution.
- Structured terminal packets are easier to audit than raw command strings buried in transcripts.
- Medium-risk commands often deserve a dry run before the real execution step.

## Minimal Code Mental Model

```python
risk = terminal_command_risk("rm -rf build", DEFAULT_DESTRUCTIVE_MARKERS)
step = terminal_packet("rg -n TODO .", cwd=".", expect_json=False)
route = terminal_route("medium", has_dry_run=True)
```

## Function

```python
DEFAULT_DESTRUCTIVE_MARKERS: list[str]

def terminal_command_risk(command: str, destructive_markers: list[str]) -> str:
def terminal_packet(command: str, cwd: str = ".", expect_json: bool = False) -> dict[str, object]:
def terminal_route(risk: str, has_dry_run: bool) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/tool-use/terminal-use/python -q
```
