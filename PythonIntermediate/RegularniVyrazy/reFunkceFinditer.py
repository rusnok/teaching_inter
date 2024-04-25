import re

iter = re.finditer(r".la", "Ola ala Ela")

for elem in iter:
    print(elem)

#pokus = re.finditer(r".la", "Ola ala Ela")
#print(list(pokus))

#print([x.span() for x in list(pokus) ])