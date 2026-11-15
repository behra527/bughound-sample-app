"""Checks that already pass. Each live bug has its own module."""

import pytest

from app.assignee_email import validate_assignee_email
from app.counts import count_open_tickets
from app.description import validate_description
from app.priority import validate_priority
from app.refs import format_ticket_ref
from app.reopen import reopen_ticket
from app.rotation import next_assignee
from app.sla import validate_sla_hours
from app.status import validate_status
from app.tags import normalize_tags
from app.validators import TicketValidationError


def test_priority_normalizes_known_value():
    assert validate_priority(" High ") == "high"


def test_priority_rejects_non_strings():
    with pytest.raises(TicketValidationError, match="string"):
        validate_priority(1)


def test_email_is_trimmed_and_lowercased():
    assert validate_assignee_email(" Ada@Example.com ") == "ada@example.com"


def test_status_normalizes_pending():
    assert validate_status(" Pending ") == "pending"


def test_sla_accepts_a_middle_value():
    assert validate_sla_hours(24) == 24


def test_sla_rejects_text():
    with pytest.raises(TicketValidationError, match="integer"):
        validate_sla_hours("24")


def test_ref_rejects_zero():
    with pytest.raises(TicketValidationError, match="positive"):
        format_ticket_ref(0)


def test_ref_starts_with_t():
    assert format_ticket_ref(3).startswith("T-")


def test_open_count_of_an_empty_list_is_zero():
    assert count_open_tickets([]) == 0


def test_reopen_rejects_a_ticket_that_is_not_closed():
    with pytest.raises(TicketValidationError, match="closed"):
        reopen_ticket({"status": "open"})


def test_tags_are_trimmed_and_lowercased():
    assert normalize_tags(["  Door "]) == ["door"]


def test_description_is_trimmed():
    assert validate_description("  Lobby door  ") == "Lobby door"


def test_rotation_stays_on_the_only_person():
    assert next_assignee(["ada"], "ada") == "ada"
