import re

pattern = r",|\."
text = "jablko,hruška,hrozny,mrkev.zelí,zelenina.ovoce,dvůr"
print(re.split(pattern, text))

pattern = r"ovoce,"
text = "jablko,hruška,hrozny,mrkev.zelí,zelenina.ovoce,dvůr"
print(re.split(pattern, text))