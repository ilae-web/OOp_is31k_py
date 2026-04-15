import re

log = "2026-04-01 ERROR Failed to connect"
match = re.search(r"(\d{4}-\d{2}-\d{2})\s+(INFO|ERROR)\s+(.+)", log)
if match:
    date, level, message = match.groups()
    print(date, level, message)