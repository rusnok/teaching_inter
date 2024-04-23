from datetime import datetime

def pust_v_rozpeti(from_=7, to_=22):
    def dek(func):
        def wrapper(*args, **kwargs):
            if from_ <= datetime.now().hour < to_:
                func(*args, **kwargs)
        return wrapper
    return dek


@pust_v_rozpeti(7, 15)
def hello(name):
    print(f"Hello, {name}")

hello("Mark")