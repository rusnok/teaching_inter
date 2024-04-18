# vlastni Exception

class Exception7(ValueError):
    pass

def nprint(n):
    if n == 7:
        raise Exception7("Fuj sedmicku nechci")
    for i in range(n):
        print(i)

nprint(3)
nprint(7)
