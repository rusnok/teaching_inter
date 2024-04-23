import csv

with open("data_textove") as in_file:
    reader = csv.reader(in_file)
    print(reader)
    for row in reader:
        print(row)

import pandas as pd

cele_data = pd.read_csv('data_textove')
print(cele_data)