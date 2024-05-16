import requests
import pandas as pd
import time
import threading

class ThreadWithReturnValue(threading.Thread):
    def __init__(self, target, args=(), kwargs={}):
        self.target = target
        self.args = args
        self.kwargs = kwargs
        super().__init__()

    def run(self):
        self.result = self.target(*self.args, **self.kwargs)

    def join(self, timeout=None):
        super().join(timeout)
        return self.result

start_date = '2024-01-01'
end_date = '2024-12-31'
all_dates = pd.date_range(start=start_date, end=end_date)
formatted_days = all_dates.strftime('%d')
formatted_months = all_dates.strftime('%m')
all_date_formatted = [a+b for a, b in zip(formatted_days, formatted_months)]

def uloz_jmena(datumy):
    list_return = []
    for datum in datumy:
        a = requests.get(f"https://svatky.adresa.info/txt?date={datum}")
        list_return.append((a.text.split(";")[-1]).rstrip())
    return list_return

dates_part = all_date_formatted


t = time.time()


if __name__ == "__main__":
    jmena = []
    threads = []
    n = 16
    step = len(dates_part)/n
    for i in range(n):
        index1 = int(i * step)
        index2 = int((i + 1) * step)
        th = ThreadWithReturnValue(target=uloz_jmena, args=(dates_part[index1:index2], ))
        th.start()
        threads.append(th)

    for th in threads:
        jmena.extend(th.join())

    print("Done!")
    print(jmena)
    print(len(jmena))

print(f"threads time: {time.time() -t}")
