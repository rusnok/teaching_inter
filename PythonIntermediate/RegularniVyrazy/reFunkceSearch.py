import re

m = re.search(r"[A-Z]la", "ala Ola Ela")
print(m)

print(m.span()[0])
print(m.group())

m = re.search(r"[A-Z]la", "ala ola ela")
print(m)
print(m.group())