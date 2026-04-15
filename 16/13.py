import re

text = "Visit https://example.com and http://test.org"
result = re.findall(r"https?://[^\s]+", text)
print(result)