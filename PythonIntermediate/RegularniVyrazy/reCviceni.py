from functools import reduce
import re

text = "test43543lfdsfdsfl534543fdgl432fr"

print(re.findall(r"\d+", text))

print(re.split(r"\d+", text))

print(re.sub(r"\d+", "", text))

print(reduce(lambda x,y: x+y, re.split(r"\d+", text)))