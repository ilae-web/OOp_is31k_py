import re

text = "apple, banana orange,grape"
result = re.split(r"[, ]+", text)
print(result)  # ['apple', 'banana', 'orange', 'grape']