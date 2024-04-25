import re

print(re.subn(r"[a-z]{5}", "pes", "Alice má slona"))

print(re.subn(r"[a-z]{4}", "pes", "Alice má slona"))