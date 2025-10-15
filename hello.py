import pandas as pd

data = pd.read_excel(r"C:\Users\dungx\Downloads\batdongsan_no_address.xlsx", engine="openpyxl")
print(data.head())  # chỉ in 5 dòng đầu để tránh tràn màn hình

import ski