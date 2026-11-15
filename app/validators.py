"""Rules for support ticket fields."""


class TicketValidationError(ValueError):
    """Raised when a customer-supplied ticket field is invalid."""


def validate_title(value: object) -> str:
    """Return a trimmed title of at most 80 characters.

    A blank or whitespace-only title raises TicketValidationError.
    """
    if not isinstance(value, str):
        raise TicketValidationError("title must be a string")

    normalized = value.strip()
    if len(normalized) > 80:
        raise TicketValidationError("title must be at most 80 characters")
    if normalized == "":
        raise TicketValidationError("title cannot be blank")
    return normalized
