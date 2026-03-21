# Model Context Protocol (MCP)

> Track: `ai-agents` | Topic: `tool-use`

## Concept

MCP is a standard way for a host and client to talk to a server that exposes tools, resources, and prompts through one structured interface.

## Key Points

- MCP separates client, host, and server responsibilities.
- Tools act, resources provide data, and prompts provide reusable prompt templates.
- Auth and session state matter because the same server may expose different capabilities to different clients.

## Minimal Code Mental Model

```python
roles = transport_roles("agent", "desktop app", "filesystem server")
caps = server_capabilities(tool_count=3, resource_count=2, prompt_count=1, auth_required=True)
session = session_context("sess_7", scopes=["repo:read"], authenticated=True)
resource = resource_read_request("repo://README.md", session_id=session["session_id"])
prompt = prompt_get_request("summarize_diff", {"style": "concise"}, session_id=session["session_id"])
tool = tool_call_request("search", {"query": "MCP overview"}, session_id=session["session_id"])
```

## Function

```python
def transport_roles(client: str, host: str, server: str) -> dict[str, str]:
def server_capabilities(
    tool_count: int = 0,
    resource_count: int = 0,
    prompt_count: int = 0,
    auth_required: bool = False,
) -> dict[str, bool]:
def session_context(session_id: str, scopes: list[str], authenticated: bool) -> dict[str, object]:
def resource_read_request(uri: str, session_id: str) -> dict[str, object]:
def prompt_get_request(name: str, arguments: dict[str, object], session_id: str) -> dict[str, object]:
def tool_call_request(name: str, arguments: dict[str, object], session_id: str) -> dict[str, object]:
```

## References

- Model Context Protocol (2025-06-18). [Overview](https://modelcontextprotocol.io/specification/2025-06-18/basic/index)
- Model Context Protocol (2025-06-18). [Authorization](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization)
- JSON-RPC Working Group. [JSON-RPC 2.0 Specification](https://www.jsonrpc.org/specification)

## Run tests

```bash
pytest modules/ai-agents/tool-use/mcp/python -q
```
