"""Assignee rotation."""

from app.validators import TicketValidationError


def next_assignee(staff: list[str], current: str) -> str:
    """Return the staff member after current, wrapping to the first.

    The function currently always returns the first person in the list.
    """
    if not isinstance(staff, list) or not staff or current not in staff:
        raise TicketValidationError("current assignee must be in the staff list")
    return staff[0]
