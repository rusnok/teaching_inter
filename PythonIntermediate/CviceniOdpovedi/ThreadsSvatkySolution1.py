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


t = time.time()
uloz_jmena(all_date_formatted, 'vsechno')
print(f"single thread time: {time.time() -t}")

t = time.time()

if __name__ == "__main__":
    t1 = threading.Thread(target=uloz_jmena, args=(all_date_formatted[:183], 'vsechno_01'))
    t2 = threading.Thread(target=uloz_jmena, args=(all_date_formatted[183:], 'vsechno_02'))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done!")

print(f"two threads time: {time.time() -t}")