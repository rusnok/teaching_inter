import re

text = "Thomas (33) and Eva (24) agreed to go shopping together tomorrow"
pattern = r"([A-Z]{1}[a-z]+) \((\d+)\)"
print(re.findall(pattern, text))