import re

# tečka
pattern = r".la"
text = "Ola ktera jedla chleba šla domů Olga Olgga, Ela"
#print(text)
#print(re.findall(pattern, text))

# otazník
pattern = r"Olg?a"
text = "Ola ktera jedla chleba šla domů Olga Olgga"
#print(text)
#print(re.findall(pattern, text))

# plus
pattern = r"a+le"
text = "Pavel alale, aaale, aaaaale Igor le aaaaaaa abcle"
#print(text)
#print(re.findall(pattern, text))

# hvězdička
pattern = r"a*le"
text = "Pavel ale, aaale, aaaaale Igor le"
#print(text)
#print(re.findall(pattern, text))

# hvězdička s otazníkem / bez otazníku
pattern = r"<.*>"
text = "<To serve man> for dinner.>"
#print(text)
#print(re.findall(pattern, text))

# hvězdička s otazníkem / bez otazníku
pattern = r"<.*?>"
text = "<To serve man> for dinner.>"
#print(text)
#print(re.findall(pattern, text))

# hranaté závorky
pattern = r"[OA]la"
text = "gOla ktera jedla chleba šla domů Olga Olgga, Ala, Ela"
#print(text)
#print(re.findall(pattern, text))

pattern = r"[a-z]la" # r"[a-ž]la"
text = "Ola ktera jedla chleba šla domů Olga Olgga, Ala, Ela"
#print(text)
#print(re.findall(pattern, text))

pattern = r"[a-]la"
text = "Ola ktera jedla chleba šla domů Olga Olgga, ala, -la"
#print(text)
#print(re.findall(pattern, text))

# kulaté závorky pro seskupení
pattern = r'First Name: (.*) Last Name: (.*)'
text = "First Name: Anna Last Name: Karenina \nFirst Name: Bob Last Name: Jones"
#print(text)
#print(re.findall(pattern, text))

# složené závorky pro opakování
pattern = r"la{2,4}"
text = "asdf Olaa laaaaa, la"
#print(text)
#print(re.findall(pattern, text))

# složené závorky pro opakování
pattern = r"a(la){1,3}"
text = "Ola zpivala alalala alalalala"
#print(text)
#print(re.findall(pattern, text))

# ^ negace
pattern = r"[^OA]la"
text = "Ola ktera jedla chleba šla domů Olga Olgga, Ala, Ela"
#print(text)
#print(re.findall(pattern, text))

# | nebo
pattern = r"Ala má (psa|kočku)"
text = "Ola má kočku, Ala má psa, Ala má levharta, Ala má kočku"
#print(text)
#print(re.findall(pattern, text))

# ^ jako počátek
pattern = r"^Ola"
text = "Ola má kočku, Ola má psa, Ola má levharta, Ala má kočku"
#print(text)
#print(re.findall(pattern, text))

# $ konec
pattern = r"Ola$"
text = f"""Ola má kočku, Ola má psa, Ola má levharta, Ala má kočku
Ola má psa.
Ola má kočku.
Igor šel domů a za ním šla Ola
Nevěděla kam jde Ola"""
print(text)
print(re.findall(pattern, text))