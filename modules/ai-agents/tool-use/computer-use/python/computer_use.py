from __future__ import annotations


TARGET_ACTIONS = {"click", "type", "scroll", "read"}
SENSITIVE_ACTIONS = {"submit", "confirm", "purchase", "send", "delete", "allow"}
DEFAULT_SENSITIVE_KEYWORDS = [
    "submit",
    "confirm",
    "purchase",
    "buy",
    "send",
    "delete",
    "allow",
    "transfer",
]
DEFAULT_UNSAFE_SCREEN_MARKERS = [
    "enter your password",
    "payment confirmation",
    "approve purchase",
    "grant access",
    "private key",
    "security code",
]


def action_requires_target(action_type: str) -> bool:
    normalized = action_type.strip().lower()
    if not normalized:
        raise ValueError("action_type must be non-empty")
    return normalized in TARGET_ACTIONS


def ui_action(action_type: str, target: str | None = None, text: str | None = None) -> dict[str, str | None]:
    normalized = action_type.strip().lower()
    if not normalized:
        raise ValueError("action_type must be non-empty")
    if action_requires_target(normalized) and not (target and target.strip()):
        raise ValueError("target is required for this action")
    if normalized == "type" and not (text and text.strip()):
        raise ValueError("text is required for type actions")
    return {
        "action": normalized,
        "target": target,
        "text": text,
    }


def step_within_budget(step_index: int, max_steps: int) -> bool:
    if step_index < 0:
        raise ValueError("step_index must be non-negative")
    if max_steps <= 0:
        raise ValueError("max_steps must be positive")
    return step_index < max_steps


def action_requires_checkpoint(
    action_type: str,
    target: str | None = None,
    sensitive_keywords: list[str] | None = None,
) -> bool:
    normalized = action_type.strip().lower()
    if not normalized:
        raise ValueError("action_type must be non-empty")

    if normalized in SENSITIVE_ACTIONS:
        return True

    if not target:
        return False

    keywords = sensitive_keywords or DEFAULT_SENSITIVE_KEYWORDS
    lowered_target = target.lower()
    return any(keyword.strip().lower() in lowered_target for keyword in keywords if keyword.strip())


def unsafe_screen_detected(screen_text: str, unsafe_markers: list[str] | None = None) -> bool:
    cleaned_text = screen_text.strip()
    if not cleaned_text:
        raise ValueError("screen_text must be non-empty")

    markers = unsafe_markers or DEFAULT_UNSAFE_SCREEN_MARKERS
    lowered = cleaned_text.lower()
    return any(marker.strip().lower() in lowered for marker in markers if marker.strip())


def should_takeover(checkpoint_required: bool, unsafe_screen: bool) -> bool:
    return checkpoint_required or unsafe_screen
