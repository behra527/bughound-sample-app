"""Rules for support ticket fields."""


class TicketValidationError(ValueError):
    """Raised when a customer-supplied ticket field is invalid."""


def validate_title(value: object) -> str:
    """Return a trimmed title of at most 80 characters."""
    if not isinstance(value, str):
        raise TicketValidationError("title must be a string")

    normalized = value.strip()
    if len(normalized) > 80:
        raise TicketValidationError("title must be at most 80 characters")
    return normalized