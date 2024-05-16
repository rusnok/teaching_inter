import requests
import pandas as pd
import time
import threading

start_date = '2024-01-01'
end_date = '2024-12-31'
all_dates = pd.date_range(start=start_date, end=end_date)
formatted_days = all_dates.strftime('%d')
formatted_months = all_dates.strftime('%m')
all_date_formatted = [a+b for a, b in zip(formatted_days, formatted_months)]

def uloz_jmena(datumy, dest):
    with open(dest, 'w') as f:
        for datum in datumy:
            a = requests.get(f"https://svatky.adresa.info/txt?date={datum}")
            f.write(a.text.split(";")[-1])

dates_part = all_date_formatted


t = time.time()


if __name__ == "__main__":
    threads = []
    n = 16
    step = len(dates_part)/n
    for i in range(n):
        index1 = int(i * step)
        index2 = int((i + 1) * step)
        th = threading.Thread(target=uloz_jmena, args=(dates_part[index1:index2], 'vsechno_'+str(i)))
        th.start()
        threads.append(th)

    for th in threads:
        th.join()

    print("Done!")

print(f"threads time: {time.time() -t}")
