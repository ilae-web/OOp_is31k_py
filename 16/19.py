import re

text = "Name: John Age: 25"
match = re.search(r"Name:\s*(\w+)\s+Age:\s*(\d+)", text)
if match:
    name, age = match.groups()
    print(name, age)  # John 25