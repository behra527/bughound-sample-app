# Support Desk Sample

Small Python service used to try BugHound with a real customer ticket.

`validate_title` trims a title and rejects titles longer than 80 characters. A blank title, or a title that is only spaces, is not rejected: the function returns `""` and `create_ticket` stores that empty title.

The product rule is different. A title must contain 1 to 80 characters after trimming. A blank title must raise `TicketValidationError`.

## Run the checks

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest -q
```