import re

print(re.match(r"[A-Z]la", "ala Ola Ela"))
print(re.match(r"[a-z]la", "ala Ola Ela"))
print(re.search(r"^[A-Z]la", "ala Ola Ela"))