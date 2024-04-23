from datetime import datetime

def pust_v_rozpeti(from_=7, to_=22):
    def dek(func):
        def wrapper():
            if from_ <= datetime.now().hour < to_:
                func()
        return wrapper
    return dek


@pust_v_rozpeti(9,23)
def pozdrav():
    print("Hello world")

pozdrav()


@pust_v_rozpeti(10, 15)
def pozdrav(name):
   print(f"Hello, {name}")

pozdrav("Mark")