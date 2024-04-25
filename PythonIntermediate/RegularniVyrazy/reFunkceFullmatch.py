import re

print(re.fullmatch(r"[A-Z]la", "Ela"))

# equivalent
print(re.search(r"^[A-Z]la$", "Ela"))