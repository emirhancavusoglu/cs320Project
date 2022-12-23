import matplotlib.pyplot as plt
from tkinter import *
import requests
import json
import os
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
bitcoin = { 'slug': 'bitcoin', 'convert': 'USD'}
binancecoin = { 'slug': 'binance-coin', 'convert': 'USD'}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '2d444a4e-7303-4551-8276-df65bb537278',
}
coins = [bitcoin,binancecoin]

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params = bitcoin)
  response2 = session.get(url, params = binancecoin)
  data = json.loads(response.text)['data']['1']['quote']['USD']['price']
  data2 = json.loads(response2.text)['data']['1839']['quote']['USD']['price']

  for i in coins :
    if (i==bitcoin):
      print(data)
    if (i==binancecoin):
      print(data2)

except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

