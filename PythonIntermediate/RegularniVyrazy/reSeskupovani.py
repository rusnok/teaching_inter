import re

text = "Thomas S. (33 l.), last seen in Krakow"
pattern = r"([A-Z]{1}[a-z]+ [A-Z]{1}\.) \((\d+) l.\)"
match = re.search(pattern, text)
print(match)
print(match.groups())
print(match.group(0))
print(match.group(1))
print(match.group(2))