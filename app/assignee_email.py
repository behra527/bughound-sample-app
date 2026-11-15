"""Assignee email rules."""

from app.validators import TicketValidationError


def validate_assignee_email(value: object) -> str:
    """Return a lowercase assignee email.

    A value with no @ sign is currently accepted and stored.
    """
    if not isinstance(value, str):
        raise TicketValidationError("email must be a string")
    normalized = value.strip().lower()
    if normalized == "":
        raise TicketValidationError("email is required")
    if "@" not in normalized:
        raise TicketValidationError("email must contain an '@' sign")
    return normalized
