def tiskni(func):
    def wrapper(*args, **kwargs):
        print("spoustim funkci")
        func(*args, **kwargs)
        print("funkce byla spustena uspesne")
    return wrapper

@tiskni
def hello(name):
    print(f"Hello, {name}")

hello("Mark")