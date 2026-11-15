"""Priority rules for a support ticket."""

from app.validators import TicketValidationError


def validate_priority(value: object) -> str:
    """Return a priority of low, medium, or high.

    Any other non-empty value is currently accepted and stored unchanged
    after it is trimmed and lowercased.
    """
    if not isinstance(value, str):
        raise TicketValidationError("priority must be a string")
    normalized = value.strip().lower()
    if normalized == "":
        raise TicketValidationError("priority is required")
    if normalized not in {"low", "medium", "high"}:
        raise TicketValidationError("unknown priority")
    return normalized
