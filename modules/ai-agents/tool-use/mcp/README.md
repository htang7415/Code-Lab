# Model Context Protocol (MCP)

> Track: `ai-agents` | Topic: `tool-use`

## Concept

MCP is a standard way for a server to expose tools, resources, and prompts to a model-driven client.

## Key Points

- MCP is about discovery and structured access, not about how the model reasons.
- A server can advertise whether it supports tools, resources, or prompts.
- Tool calls still need ordinary validation and feedback loops after discovery.

## Minimal Code Mental Model

```python
caps = server_capabilities(tool_count=3, resource_count=2, prompt_count=1)
tool = tool_descriptor("search", "Search documents")
request = tool_call_request("search", {"query": "MCP overview"})
```

## Function

```python
def server_capabilities(tool_count: int = 0, resource_count: int = 0, prompt_count: int = 0) -> dict[str, bool]:
def tool_descriptor(name: str, description: str) -> dict[str, str]:
def tool_call_request(name: str, arguments: dict[str, object]) -> dict[str, object]:
```

## Run tests

```bash
pytest modules/ai-agents/tool-use/mcp/python -q
```
