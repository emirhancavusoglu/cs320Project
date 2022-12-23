import tkinter

import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
import numpy as np
import requests
import json
import os
import self as self
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

root = Tk()
root.title("Split Portfolio")
# root.iconbitmap(r'SP.ico')
root.geometry("500x500")
root.resizable(width=False, height=False)

# Header
lb1 = Label(root, text="Your Assets")
lb1.config(font=('helvetica', 25))
lb1.place(relx=0.5, rely=0.1, anchor=CENTER)

# currency label
lb2 = Label(root, text="Currency", font=("arial", 12))
lb2.place(x=135, y=118)

# combobox
currencylist = ["BTC", "ETH", "BNB", "XRP", "DogeCoin", "LightCoin", "Cardano", "Solana", "Shiba Inu", "Polkadot"]
Combo = ttk.Combobox(root, state="readonly", values=currencylist)
Combo.place(x=240, y=118)

# Amount label
lb3 = Label(root, text="Amount", font=("arial", 12))
lb3.place(x=135, y=157)

# Amount entry label
en2 = Entry(root, width=23)
en2.place(x=240, y=160)

# If several currencies will be added
currency = []
amount = []


def continue_adding():
    currency.append(Combo.current())
    amount.append(int(en2.get()))
    print(currency, amount)
    Combo.set("")
    en2.delete(0, END)


# Add Button
add_btn = Button(root, text='ADD', height=3, width=20, command=continue_adding)
add_btn.place(relx=0.5, rely=0.50, anchor=CENTER)


def open_Shares_Page():
    shares_page = Toplevel(root)
    shares_page.title("Split Portfolio")
    shares_page.geometry("800x800")
    shares_page.resizable(width=False, height=False)
    new_currency = transform(currency)
    print(new_currency)
    header_name = Label(shares_page, text="Name", bg="white", font="Verdana 8 bold")
    header_name.grid(row=0, column=0, sticky=N + S + E + W)

    header_rank = Label(shares_page, text="Rank", bg="silver", font="Verdana 8 bold")
    header_rank.grid(row=0, column=1, sticky=N + S + E + W)

    header_current_price = Label(shares_page, text="Current Price", bg="white", font="Verdana 8 bold")
    header_current_price.grid(row=0, column=2, sticky=N + S + E + W)

    header_1_hr_change = Label(shares_page, text="1 HR Change", bg="silver", font="Verdana 8 bold")
    header_1_hr_change.grid(row=0, column=5, sticky=N + S + E + W)

    header_24_hr_change = Label(shares_page, text="24 HR Change", bg="white", font="Verdana 8 bold")
    header_24_hr_change.grid(row=0, column=6, sticky=N + S + E + W)

    header_7_day_change = Label(shares_page, text="7 Day Change", bg="silver", font="Verdana 8 bold")
    header_7_day_change.grid(row=0, column=7, sticky=N + S + E + W)

    header_current_value = Label(shares_page, text="Current Value", bg="white", font="Verdana 8 bold")
    header_current_value.grid(row=0, column=8, sticky=N + S + E + W)


# Continue Button
continue_btn = Button(root, text='CONTINUE', height=3, width=20, command=open_Shares_Page)
continue_btn.place(relx=0.5, rely=0.65, anchor=CENTER)


def transform(currency):
    new_currency = []
    for val in currency:
        if val == 0:
            new_currency.append("BTC")
        if val == 1:
            new_currency.append("ETH")
        if val == 2:
            new_currency.append("BNB")
        if val == 3:
            new_currency.append("XRP")
        if val == 4:
            new_currency.append("DogeCoin")
        if val == 5:
            new_currency.append("LightCoin")
        if val == 6:
            new_currency.append("Cardano")
        if val == 7:
            new_currency.append("Solana")
        if val == 8:
            new_currency.append("Shiba Inu")
        if val == 9:
            new_currency.append("Polkadot")
    return new_currency


root.mainloop()

url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
<<<<<<< HEAD

parameters = {'slug': 'bitcoin', 'convert': 'USD'}

=======
>>>>>>> 0b6249a5e68a1c4c62ee3ac4d1ec1ca8e5353376
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

<<<<<<< HEAD
# try:
# response = session.get(url, params=parameters)
# data = json.loads(response.text)['data']['1']['quote']['USD']['price']
# print(data)


# except (ConnectionError, Timeout, TooManyRedirects) as e:
# print(e)
=======
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
>>>>>>> 0b6249a5e68a1c4c62ee3ac4d1ec1ca8e5353376
