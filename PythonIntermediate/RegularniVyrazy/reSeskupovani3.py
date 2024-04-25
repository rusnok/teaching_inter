import re

pattern = r"a(la){4}"
text = "Ola zpivala alalala alalalala"
print(text)
print(re.findall(pattern, text))

m = re.search(pattern, text)
print(m)
print(m.group(0))
print(m.group(1))
print(m.groups())

