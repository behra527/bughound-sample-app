"""Reopen a closed ticket."""

from app.validators import TicketValidationError


def reopen_ticket(ticket: dict) -> dict:
    """Return a copy of a closed ticket with status open.

    The copy currently keeps the old status, so a closed ticket stays closed.
    """
    if not isinstance(ticket, dict) or ticket.get("status") != "closed":
        raise TicketValidationError("only a closed ticket can be reopened")
    updated = dict(ticket)
    updated["status"] = ticket["status"]
    return updated
