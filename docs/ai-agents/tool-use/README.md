# Tool Use

This section is about how an agent decides to call tools, how computer-use loops differ from ordinary API tools, and where MCP fits.

## Purpose

Use this page to keep tool-using agents in the right order:
- basic structured tool calls
- computer-use actions over a UI
- MCP as a standard way to expose tools and resources

## First Principles

- Tool use is about deciding when the model should act outside pure text generation.
- Computer use is a special case where the agent acts over a changing interface instead of a fixed function API.
- MCP is a transport and discovery layer for tools, resources, and prompts, not a reasoning policy by itself.
- Good tool use needs structure, validation, and short feedback loops.

## Minimal Code Mental Model

```python
tool = select_tool(user_intent, tool_keywords)
call = tool_call(tool, arguments)
result = tool_result(call["id"], output)
```

## Canonical Modules

- Core function calling: `tool-use-basics`
- UI action loops: `computer-use`
- Standardized tool and resource exposure: `mcp`

## When To Use What

- Start with `tool-use-basics` when the problem is ordinary function calling.
- Use `computer-use` when the agent must click, type, scroll, or inspect a live interface.
- Use `mcp` when tools and resources need a standard server-style interface instead of one-off adapters.
