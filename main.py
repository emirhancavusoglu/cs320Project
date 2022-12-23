import matplotlib.pyplot as plt
from tkinter import *
import requests
import json
import os
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '2d444a4e-7303-4551-8276-df65bb537278',
}
bitcoin = { 'symbol': 'BTC', 'convert': 'USD'}
ethereum = { 'symbol': 'ETH', 'convert': 'USD'}
bnb = { 'symbol': 'BNB', 'convert': 'USD'}
xrp = { 'symbol': 'XRP', 'convert': 'USD'}
dogecoin = { 'symbol': 'DOGE', 'convert': 'USD'}
cardano = { 'symbol': 'ADA', 'convert': 'USD'}
litecoin = { 'symbol': 'LTC', 'convert': 'USD'}
solana = { 'symbol': 'SOL', 'convert': 'USD'}
shiba = { 'symbol': 'SHIB', 'convert': 'USD'}
polkadot = { 'symbol': 'DOT', 'convert': 'USD'}

coins = []

parameters = {
  'symbol': 'BTC,ETH,BNB,XRP,DOGE,ADA,LTC,SOL,SHIB,DOT'
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  #response2 = session.get(url, params=ethereum)


  data = json.loads(response.text)['data']
  #data2 = json.loads(response2.text)['data']

  print("Enter the value that you want to enter share")
  miktar = int(input())

  for ix in range(miktar):
    share = int(input())
    coins.insert(ix, share)

  for i in coins:
    if (i == 1):
      print(data)


except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)