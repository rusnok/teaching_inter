def sudociselny_generator(n):
    cislo = 2
    vygenerovana_cisla = 0
    while vygenerovana_cisla != n:
        if cislo % 2 == 0:
            yield cislo
            vygenerovana_cisla += 1
        cislo += 1


gen = sudociselny_generator(3)
for elem in gen:
    print(elem)