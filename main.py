import tkinter
from datetime import datetime

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
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pprint
import os
import csv
import pandas as pd

def red_green(amount):
    if amount >= 0:
        return "green"
    else:
        return "red"


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
currencylist = ["BTC", "ETH", "BNB", "XRP", "DOGE", "LTC", "ADA", "SOL", "SHIB", "DOT"]
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
<<<<<<< HEAD
    currency_toIn = Combo.current()
=======
    currency_toIn= Combo.current()
>>>>>>> 43cb22e35ee48cb0e40138388cf801f51258bab4
    if currency_toIn in currency:
        index = currency.index(currency_toIn)
        print("Already in")
        if len(en2.get()) == 0:
            print("sa")
        else:
<<<<<<< HEAD
            sum = int(en2.get()) + amount[index]
            amount[index] = sum;
=======
            sum = int(en2.get())+amount[index]
            amount[index]= sum
>>>>>>> 43cb22e35ee48cb0e40138388cf801f51258bab4
            print(currency, amount)
            Combo.set("")
            en2.delete(0, END)
    else:
        currency.append(currency_toIn)
        if len(en2.get()) == 0:
            amount.append('0')
        else:
            amount.append(int(en2.get()))
            print(currency, amount)
            Combo.set("")
            en2.delete(0, END)
<<<<<<< HEAD

=======
>>>>>>> 43cb22e35ee48cb0e40138388cf801f51258bab4


# Add Button
add_btn = Button(root, text='ADD', height=3, width=20, command=continue_adding)
add_btn.place(relx=0.5, rely=0.50, anchor=CENTER)

new_currency = []
def open_Shares_Page():
    shares_page = Toplevel(root)
    shares_page.title("Split Portfolio")
    shares_page.geometry("800x800")
    shares_page.resizable(width=False, height=False)
    new_currency = transform(currency)
    print(new_currency)

    header_name = Label(shares_page, text="Name", bg="white", width= 15, font="Verdana 8 bold")
    header_name.place(x=0,y=400)


    header_rank = Label(shares_page, text="Rank", bg="silver", width= 10, font="Verdana 8 bold")
    header_rank.place(x=120,y=400)

    header_current_price = Label(shares_page, text="Current Price", bg="white", width=13, font="Verdana 8 bold")
    header_current_price.place(x=205,y=400)

    header_1_hr_change = Label(shares_page, text="1 HR Change", bg="silver", width=12, font="Verdana 8 bold")
    header_1_hr_change.place(x=315,y=400)

    header_24_hr_change = Label(shares_page, text="24 HR Change", bg="white", width=12, font="Verdana 8 bold")
    header_24_hr_change.place(x=410,y=400)

<<<<<<< HEAD
    header_7_day_change = Label(shares_page, text="7 Day Change", bg="silver", width=12, font="Verdana 8 bold")
    header_7_day_change.place(x=510,y=400)

    header_amount = Label(shares_page, text="Amount", bg="white", width= 10, font="Verdana 8 bold")
    header_amount.place(x=610,y=400)

    header_current_value = Label(shares_page, text="Current Value", bg="silver", width=13, font="Verdana 8 bold")
    header_current_value.place(x=690,y=400)
=======
    header_amount=Label(shares_page,text="Amount",bg="white", font="Verdana 8 bold")
    header_amount.grid(row=0, column=8, sticky=N + S + E + W)

    header_current_value = Label(shares_page, text="Current Value", bg="silver", font="Verdana 8 bold")
    header_current_value.grid(row=0, column=9, sticky=N + S + E + W)
>>>>>>> 43cb22e35ee48cb0e40138388cf801f51258bab4

    symbolstr = ','.join(('BTC,ETH,BNB,XRP,USDT,ADA,DOT,UNI,LTC,LINK,XLM,BCH',
                          'THETA,FIL,USDC,TRX,DOGE,WBTC,VET,SOL,KLAY,EOS,XMR,LUNA',
                          'MIOTA,BTT,CRO,BUSD,FTT,AAVE,BSV,XTZ,ATOM,NEO,AVAX,ALGO',
                          'CAKE,HT,EGLD,XEM,KSM,BTCB,DAI,HOT,CHZ,DASH,HBAR,RUNE,MKR,ZEC',
                          'ENJ,DCR,MKR,ETC,GRT,COMP,STX,NEAR,SNX,ZIL,BAT,LEO,SUSHI',
                          'MATIC,BTG,NEXO,TFUEL,ZRX,UST,CEL,MANA,YFI,UMA,WAVES,RVN',
                          'ONT,ICX,QTUM,ONE,KCS,OMG,FLOW,OKB,BNT,HNT,SC,DGB,RSR,DENT',
                          'ANKR,REV,NPXS,VGX,FTM,CHSB,REN,IOST,BTMX,CELO,PAX,CFX,SHIB'))


    symbol_list = symbolstr.split(',')
    key = os.environ.get('')

    url = f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    print(url)
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '698e8ff5-6293-4eac-a0f3-b8df83d683e9'
    }
    parameters = {
        'symbol': symbolstr
    }
    session = Session()
    session.headers.update(headers)


    response = session.get(url, params=parameters)
    data = json.loads(response.text)['data']

    row_count = 1
    count = 0

    for i in new_currency:

<<<<<<< HEAD
        x = 0
=======
>>>>>>> 43cb22e35ee48cb0e40138388cf801f51258bab4

        current_value = float(amount[count]) * float(data[i]['quote']['USD']['price'])

        name = Label(shares_page, text=data[i]['name'], bg="white")
        name.grid(row=row_count, column=0, sticky=N + S + E + W)

        rank = Label(shares_page, text=data[i]['cmc_rank'], bg="silver")
        rank.grid(row=row_count, column=1, sticky=N + S + E + W)

        current_price = Label(shares_page, text="${0:.2f}".format(float(data[i]['quote']['USD']['price'])), bg="white", )
        current_price.grid(row=row_count, column=2, sticky=N + S + E + W)

        one_hr_change = Label(shares_page, text="{0:.2f}%".format(float(data[i]['quote']['USD']['percent_change_60d'])),
                              bg="silver",
                              fg=red_green(float(data[i]['quote']['USD']["percent_change_60d"])))
        one_hr_change.grid(row=row_count, column=5, sticky=N + S + E + W)

        tf_hr_change = Label(shares_page, text="{0:.2f}%".format(float(data[i]['quote']['USD']['percent_change_24h'])),
                                 bg="white",
                                 fg=red_green(float(data[i]['quote']['USD']["percent_change_24h"])))
        tf_hr_change.grid(row=row_count, column=6, sticky=N + S + E + W)

        seven_day_change = Label(shares_page, text="{0:.2f}%".format(float(data[i]['quote']['USD']['percent_change_7d'])),
                                     bg="silver",
                                     fg=red_green(float(data[i]['quote']['USD']["percent_change_7d"])))
        seven_day_change.grid(row=row_count, column=7, sticky=N + S + E + W)

        amountLabel = Label(shares_page,text="{0:.2f}".format(amount[count]), bg="white")
        amountLabel.grid(row=row_count,column=8,sticky=N + S + E + W)

        current_value = Label(shares_page, text="${0:.2f}".format(float(current_value)), bg="silver")
        current_value.grid(row=row_count, column=9, sticky=N + S + E + W)

        row_count += 1
        count += 1

<<<<<<< HEAD
        def showFuturePrice():
            global futurePrice
            futurePanel = Toplevel(root)
            futurePanel.title("Estimated Future Price")
            futurePanel.geometry("400x400")
            futurePanel.resizable(width=False, height=False)
            hss = Label(futurePanel, text="Estimated Future Price", bg="white", font="Verdana 8 bold")
            hss.grid(row=0, column=0, sticky=N + S + E + W)
            row_count_future = 0
            column_count_future = 15
            for i in new_currency:
                futurePrice = float(data[i]['quote']['USD']['price']) * (
                            float(data[i]['quote']['USD']['percent_change_7d']) - float(
                        data[i]['quote']['USD']["percent_change_24h"]))
                if futurePrice < 0:
                    futurePrice = 0

                future_price_button_name = Label(futurePanel, text=data[i]['name'], bg="white")
                future_price_button_name.place(x=0, y=column_count_future)

                future_price_button_price = Label(futurePanel, text=futurePrice, bg="white", font="Verdana 8 bold")
                future_price_button_price.place(x=60, y=column_count_future)
                column_count_future += 20

    future_price_button = Button(shares_page, text="Estimated Future Price", command=showFuturePrice)
    future_price_button.grid(row=row_count + 1, column=9, sticky=E + S, padx=10,pady = 10)

=======
>>>>>>> 43cb22e35ee48cb0e40138388cf801f51258bab4
    def don(event=None):
        shares_page.destroy()
        open_Shares_Page()

    update_button = Button(shares_page, text="Update Prices", command=don)
    update_button.grid(row=row_count, column=9, sticky=E + S, padx=10, pady=10)


<<<<<<< HEAD
=======
    #update_button = Button(self.root, text="Update", command=)
    #update_button.grid(row=row_count, column=9, sticky=E + S, padx=10, pady=10)
>>>>>>> 43cb22e35ee48cb0e40138388cf801f51258bab4
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
            new_currency.append("DOGE")
        if val == 5:
            new_currency.append("LTC")
        if val == 6:
            new_currency.append("ADA")
        if val == 7:
            new_currency.append("SOL")
        if val == 8:
            new_currency.append("SHIB")
        if val == 9:
            new_currency.append("DOT")
    return new_currency

<<<<<<< HEAD
root.mainloop()
=======
root.mainloop()
>>>>>>> 43cb22e35ee48cb0e40138388cf801f51258bab4
