# Support Desk Sample

Small Python service used to try BugHound with a real customer ticket.

A support agent creates a ticket with a title and a description. Titles are trimmed. A title must contain 1 to 80 characters after trimming. A blank title, or a title that is only spaces, must be rejected. Descriptions are required.

## Run the checks

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest -q
```

`tests/test_tickets.py::test_blank_titles_are_rejected` currently fails. Creating a ticket with `""` or `"   "` is stored with an empty title instead of being rejected.
