from __future__ import annotations

DEFAULT_DESTRUCTIVE_MARKERS = [
    "rm -rf",
    "git push --force",
    "chmod -r",
    "mkfs",
    "dd if=",
    "shutdown",
    "reboot",
]

_MEDIUM_RISK_MARKERS = [
    "sudo ",
    " install ",
    ">>",
    " > ",
    "curl ",
    "wget ",
]


def terminal_command_risk(command: str, destructive_markers: list[str]) -> str:
    cleaned_command = command.strip()
    if not cleaned_command:
        raise ValueError("command must be non-empty")

    lowered = f" {cleaned_command.lower()} "
    for marker in destructive_markers:
        candidate = marker.strip().lower()
        if candidate and candidate in lowered:
            return "high"

    for marker in _MEDIUM_RISK_MARKERS:
        if marker in lowered:
            return "medium"
    return "low"


def terminal_packet(command: str, cwd: str = ".", expect_json: bool = False) -> dict[str, object]:
    cleaned_command = command.strip()
    cleaned_cwd = cwd.strip()
    if not cleaned_command:
        raise ValueError("command must be non-empty")
    if not cleaned_cwd:
        raise ValueError("cwd must be non-empty")

    return {
        "command": cleaned_command,
        "cwd": cleaned_cwd,
        "expect_json": expect_json,
    }


def terminal_route(risk: str, has_dry_run: bool) -> str:
    cleaned_risk = risk.strip().lower()
    if cleaned_risk not in {"low", "medium", "high"}:
        raise ValueError("risk must be low, medium, or high")
    if cleaned_risk == "high":
        return "review"
    if cleaned_risk == "medium":
        return "dry-run" if has_dry_run else "review"
    return "execute"
