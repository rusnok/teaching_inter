from datetime import datetime

def vypni_v_noci(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()

    return wrapper

#pozdrav = vypni_v_noci(pozdrav)

@vypni_v_noci
def pozdrav():
    print("Hello world")


pozdrav()