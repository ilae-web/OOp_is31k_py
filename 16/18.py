import re

card = "1234 5678 9012 3456"
result = re.sub(r"\d{4}(?=\s|$)", "****", card)
print(result)  # **** **** **** 3456