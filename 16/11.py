import re

text = "a cat and a dog run fast"
result = re.sub(r"\b\w{1,2}\b", "****", text)
print(result)