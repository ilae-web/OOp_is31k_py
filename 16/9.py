import re

password = "Pass1234"
result = len(password) >= 8 and bool(re.search(r"\d", password))
print(result)  # True