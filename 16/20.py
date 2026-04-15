import re
from collections import Counter

logs = """2026-04-01 ERROR Failed
2026-04-01 INFO OK
2026-04-02 ERROR Crash"""

error_dates = re.findall(r"(\d{4}-\d{2}-\d{2})\s+ERROR", logs)
count_by_date = Counter(error_dates)

for date, count in count_by_date.items():
    print(f"{date}: {count}")