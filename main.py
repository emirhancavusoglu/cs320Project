import matplotlib.pyplot as plt
from tkinter import *
import requests
import json
import os
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
parameters = { 'slug': 'binance-coin', 'convert': 'USD'}

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '2d444a4e-7303-4551-8276-df65bb537278',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params = parameters)
  data = json.loads(response.text)['data']['1']['quote']['USD']['price']
  print(data)






except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

