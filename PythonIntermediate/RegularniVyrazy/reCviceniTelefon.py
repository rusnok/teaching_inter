import re
text = ("48123456789", "+48123456789", "0048123456789a", "asdf", "123456")
pattern = r"(48)|(\+48)|(0048)\d{9}"
pattern2 = "(\+|00)?48\d{9}"


for t in text:
    print(f"{t}, {bool(re.match(pattern, t))}")
    print(f"{t}, {bool(re.fullmatch(pattern2, t))}")

