import re

print(re.findall(r".la", "Ola ala Ela"))

p = re.compile(r".la")
print(p.findall("Ola ala Ela"))
print(p.match("Ola ala Ela"))