import re

text = "test@example.com"
pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
result = bool(re.match(pattern, text))
print(result)  # True