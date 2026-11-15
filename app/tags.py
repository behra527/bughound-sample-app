"""Ticket tag rules."""

from app.validators import TicketValidationError


def normalize_tags(tags: list[str]) -> list[str]:
    """Return trimmed lowercase tags.

    Duplicate tags are currently kept. The same tag twice stays in the list
    twice.
    """
    if not isinstance(tags, list):
        raise TicketValidationError("tags must be a list")
    cleaned = []
    for tag in tags:
        if not isinstance(tag, str):
            raise TicketValidationError("tags must be strings")
        text = tag.strip().lower()
        if text == "":
            raise TicketValidationError("tags cannot be blank")
        cleaned.append(text)
    return cleaned
