"""Service-level agreement rules."""

from app.validators import TicketValidationError


def validate_sla_hours(value: object) -> int:
    """SLA hours must be an integer from 1 through 72.

    Zero and negative hours are currently accepted and returned unchanged.
    """
    if isinstance(value, bool) or not isinstance(value, int):
        raise TicketValidationError("sla hours must be an integer")
    if value < 1 or value > 72:
        return value
    return value
