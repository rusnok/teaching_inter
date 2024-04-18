def moje_funkce():
    a = 3
    b = [1, 0, 2]
    for elem in b:
        if elem == 0:
            raise ValueError("The divisor cannot be zero, chapes?")
        result = a / elem
        print(f"Result is: {result}")
moje_funkce()
#try:
#    moje_funkce()
#except ValueError:
#    print("kolega programoval zvlastne")