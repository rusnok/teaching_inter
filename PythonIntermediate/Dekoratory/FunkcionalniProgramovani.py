print(len("asdf"))
moje_len = len

print(moje_len("asdf"))

def druha_mocnina(x):
    return x**2

def treti_mocnina(x):
    return x**3

print(druha_mocnina(3))
print(treti_mocnina(4))

def x_mocnina(n):
    def mocnina(x):
        return x**n

    return mocnina

print("******************************")
print("Sofistikovane generovani mocnin")
moje_mocnina = x_mocnina(2)
print(moje_mocnina(4))

def x_plus(n):
    def jakkoliv(x):
        return x + n

    return jakkoliv

print("******************************")
print("Sofistikovane generovani plusu")
moje_plus = x_plus(100000)
print(moje_plus(4))
print(moje_plus(10))
print(moje_plus(100))

print("---------------")
print(x_mocnina(1/2)(16))