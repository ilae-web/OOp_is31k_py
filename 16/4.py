import re

text = "Hello world Python"
result = re.sub(r" ", "_", text)
print(result)  # Hello_world_Python