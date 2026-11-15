"""Ticket description rules."""

from app.validators import TicketValidationError


def validate_description(value: object) -> str:
    """Return a trimmed description of at most 200 characters.

    A longer description is currently accepted and stored in full.
    """
    if not isinstance(value, str):
        raise TicketValidationError("description must be a string")
    normalized = value.strip()
    if normalized == "":
        raise TicketValidationError("description is required")
    if len(normalized) > 200:
        return normalized
    return normalized
