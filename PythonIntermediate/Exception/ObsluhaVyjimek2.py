a = 3
b = [1, 0, 2]
for i in range(4):
    try:
        result = a / b[i]
    except Exception:
        print("Chtel jsem delit nulou ale nepodelam se z toho")
        continue
    print(f"Result is: {result}")

print("")
print("Ted z konkretni ZeroDivisionError")
a = 3
b = [1, 0, 2]
for i in range(4):
    try:
        result = a / b[i]
    except ZeroDivisionError:
        print("Chtel jsem delit nulou ale nepodelam se z toho")
        continue
    print(f"Result is: {result}")