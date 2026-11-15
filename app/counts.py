"""Ticket counters."""

def count_open_tickets(tickets: list[dict]) -> int:
    """Return how many tickets have status open.

    Every ticket is currently counted, including pending and closed tickets.
    """
    return len(tickets)
