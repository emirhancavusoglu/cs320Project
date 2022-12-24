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
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pprint
import os
import csv


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
    currency.append(Combo.current())
    amount.append(int(en2.get()))
    print(currency, amount)
    Combo.set("")
    en2.delete(0, END)


# Add Button
add_btn = Button(root, text='ADD', height=3, width=20, command=continue_adding)
add_btn.place(relx=0.5, rely=0.50, anchor=CENTER)

new_currency = []
shares_page = Toplevel(root)


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
        'X-CMC_PRO_API_KEY': '2d444a4e-7303-4551-8276-df65bb537278'
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
        current_value = float(amount[count]) * float(data[i]['quote']['USD']['price'])

        #print(data[i]['name'])
        #print("${0:.2f}".format(float(data[i]['quote']['USD']['price'])))
        #print("Rank: {0:.0f}".format(float(data[i]['cmc_rank'])))
        #print("Current Value: ${0:.2f}".format(float(current_value)))

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

        current_value = Label(shares_page, text="${0:.2f}".format(float(current_value)), bg="white")
        current_value.grid(row=row_count, column=8, sticky=N + S + E + W)

        row_count += 1
        count += 1

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

root.mainloop()
#tugberk
