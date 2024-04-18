try:
    x = 10
    if x == 10:
        print("x je 10")
        1/0
    else:
        print("x není 10")
except ValueError:
    print("Zadej jinou hodnotu do funkce")
except (ZeroDivisionError, KeyError):
    print("Mas chybu v datech")
finally:
    print("Gratuluji dospel jsi do konce kodu")