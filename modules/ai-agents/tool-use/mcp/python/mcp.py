from __future__ import annotations


def server_capabilities(
    tool_count: int = 0,
    resource_count: int = 0,
    prompt_count: int = 0,
    auth_required: bool = False,
) -> dict[str, bool]:
    counts = [tool_count, resource_count, prompt_count]
    if any(count < 0 for count in counts):
        raise ValueError("counts must be non-negative")
    return {
        "tools": tool_count > 0,
        "resources": resource_count > 0,
        "prompts": prompt_count > 0,
        "auth": auth_required,
    }


def transport_roles(client: str, host: str, server: str) -> dict[str, str]:
    cleaned_client = client.strip()
    cleaned_host = host.strip()
    cleaned_server = server.strip()
    if not cleaned_client:
        raise ValueError("client must be non-empty")
    if not cleaned_host:
        raise ValueError("host must be non-empty")
    if not cleaned_server:
        raise ValueError("server must be non-empty")
    return {
        "client": cleaned_client,
        "host": cleaned_host,
        "server": cleaned_server,
    }


def session_context(session_id: str, scopes: list[str], authenticated: bool) -> dict[str, object]:
    cleaned_session_id = session_id.strip()
    if not cleaned_session_id:
        raise ValueError("session_id must be non-empty")
    cleaned_scopes = sorted({scope.strip() for scope in scopes if scope.strip()})
    return {
        "session_id": cleaned_session_id,
        "scopes": cleaned_scopes,
        "authenticated": authenticated,
    }


def resource_read_request(uri: str, session_id: str) -> dict[str, object]:
    cleaned_uri = uri.strip()
    cleaned_session_id = session_id.strip()
    if not cleaned_uri:
        raise ValueError("uri must be non-empty")
    if not cleaned_session_id:
        raise ValueError("session_id must be non-empty")
    return {
        "method": "resources/read",
        "params": {
            "uri": cleaned_uri,
            "session_id": cleaned_session_id,
        },
    }


def prompt_get_request(name: str, arguments: dict[str, object], session_id: str) -> dict[str, object]:
    if not name.strip():
        raise ValueError("name must be non-empty")
    if not session_id.strip():
        raise ValueError("session_id must be non-empty")
    return {
        "method": "prompts/get",
        "params": {
            "name": name,
            "arguments": arguments,
            "session_id": session_id,
        },
    }


def tool_call_request(name: str, arguments: dict[str, object], session_id: str) -> dict[str, object]:
    if not name.strip():
        raise ValueError("name must be non-empty")
    if not session_id.strip():
        raise ValueError("session_id must be non-empty")
    return {
        "method": "tools/call",
        "params": {
            "name": name,
            "arguments": arguments,
            "session_id": session_id,
        },
    }
