"""Support ticket creation."""

from app.validators import TicketValidationError, validate_title


def create_ticket(title: object, description: object) -> dict:
    """Create an open ticket from a title and description."""
    if not isinstance(description, str) or not description.strip():
        raise TicketValidationError("description is required")

    return {
        "title": validate_title(title),
        "description": description.strip(),
        "status": "open",
    }