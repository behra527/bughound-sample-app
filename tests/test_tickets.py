"""Ticket title checks that pass on the current code."""

import pytest

from app.tickets import create_ticket
from app.validators import TicketValidationError, validate_title


def test_title_is_trimmed():
    assert validate_title("  Printer jam  ") == "Printer jam"


def test_title_accepts_maximum_length():
    assert validate_title("x" * 80) == "x" * 80


def test_title_rejects_overlong_values():
    with pytest.raises(TicketValidationError, match="80"):
        validate_title("x" * 81)


def test_title_rejects_non_strings():
    with pytest.raises(TicketValidationError, match="string"):
        validate_title(42)


def test_create_ticket_stores_trimmed_title():
    ticket = create_ticket("  Door lock  ", "  Lobby door will not latch  ")
    assert ticket == {
        "title": "Door lock",
        "description": "Lobby door will not latch",
        "status": "open",
    }