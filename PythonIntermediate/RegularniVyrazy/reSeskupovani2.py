import re

text = "Thomas (33) and Eva (24) agreed to go Pavel (34 shopping together tomorrow Igor (37) "
pattern = r"([A-Z]{1}[a-z]+) \((\d+)\)"
print(re.findall(pattern, text))