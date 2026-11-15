"""Public ticket references."""

from app.validators import TicketValidationError


def format_ticket_ref(ticket_id: int) -> str:
    """Return the public reference for a ticket id.

    The first ticket, id 1, should be T-1. The function currently subtracts
    one, so id 1 is returned as T-0.
    """
    if isinstance(ticket_id, bool) or not isinstance(ticket_id, int) or ticket_id < 1:
        raise TicketValidationError("ticket id must be a positive integer")
    return f"T-{ticket_id - 1}"
