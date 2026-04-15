import re

text = "hello world python"
result = re.sub(r"\b\w", lambda m: m.group(0).upper(), text)
print(result)  # Hello World Python