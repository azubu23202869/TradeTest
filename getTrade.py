import requests
import pandas as pd

url = "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date=20200224&stockNo=2330"
data = pd.read_html(requests.get(url).text)[0]

print(data)