import requests
import pandas as pd




def generator_jmen(n):
    start_date = '2024-01-01'
    end_date = '2024-12-31'
    all_dates = pd.date_range(start=start_date, end=end_date)
    formatted_days = all_dates.strftime('%d')
    formatted_months = all_dates.strftime('%m')
    all_date_formatted = [a + b for a, b in zip(formatted_days, formatted_months)]


    index = 0
    while index != n:
        a = requests.get(f"https://svatky.adresa.info/txt?date={all_date_formatted[index]}")
        yield a.text.split(";")[-1].rstrip()
        index += 1


for j in generator_jmen(30):
    print(j)