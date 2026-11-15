"""Ticket status rules."""

from app.validators import TicketValidationError


def validate_status(value: object) -> str:
    """Return open, pending, or closed.

    Any other non-empty status is currently accepted and stored.
    """
    if not isinstance(value, str):
        raise TicketValidationError("status must be a string")
    normalized = value.strip().lower()
    if normalized == "":
        raise TicketValidationError("status is required")
    if normalized not in {"open", "pending", "closed"}:
        return normalized
    return normalized
