a = 3
b = [1, 0, 2]
for elem in b:
    try:
        result = a / elem
    except ZeroDivisionError as e:
        print(str(e))
        print(type(e))
        print("Chtel jsem delit nulou ale nepodelam se z toho")
        continue
    print(f"Result is: {result}")