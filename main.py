import datetime
from tkinter import *
from tkinter import ttk

import requests
from matplotlib import pyplot as plt
from requests import Request, Session
import json
import os
import webview
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


def infoShow(event=None):
    infoPanel = Toplevel(root)
    infoPanel.title("Guide")
    infoPanel.geometry("930x200")
    infoPanel.resizable(width=False, height=False)

    infoLabel1 = Label(infoPanel, text="1- Choose the name of the owned coin.", font="Verdana 8 bold")
    infoLabel1.place(x=0, y=10)

    infoLabel2 = Label(infoPanel, text="2- Enter the amount of coins owned.", font="Verdana 8 bold")
    infoLabel2.place(x=0, y=30)

    infoLabel3 = Label(infoPanel,
                       text="3- Then it can be added to the portfolio by clicking the ""ADD"" button. This operation can be done as desired.",
                       font="Verdana 8 bold")
    infoLabel3.place(x=0, y=50)

    infoLabel4 = Label(infoPanel,
                       text="4- By clicking the ""Continue"" button, you can go to the other page and see the instant data and charts of the coins owned.",
                       font="Verdana 8 bold")
    infoLabel4.place(x=0, y=70)

    infoLabel5 = Label(infoPanel,
                       text="5- By clicking the ""Estimated Future Price"" button, the estimated future prices of the selected coins can be seen according to our algorithm.",
                       font="Verdana 8 bold")
    infoLabel5.place(x=0, y=90)

    infoLabel6 = Label(infoPanel, text="6- By clicking the ""Show News"" button, the news of the coins can be seen.",
                       font="Verdana 8 bold")
    infoLabel6.place(x=0, y=110)

    infoLabel7 = Label(infoPanel,
                       text="7- By clicking the ""Pie Chart"" button, the amount of coins in the portfolio can be seen on the pie chart.",
                       font="Verdana 8 bold")
    infoLabel7.place(x=0, y=130)

    infoLabel8 = Label(infoPanel,
                       text="8- By pressing the ""Update Prices"" button, the price of the coins is updated.",
                       font="Verdana 8 bold")
    infoLabel8.place(x=0, y=150)

    infoLabel9 = Label(infoPanel,
                       text="9- By pressing the ""Change Currency"" button, the values of the coins can be seen according to the selected currency.",
                       font="Verdana 8 bold")
    infoLabel9.place(x=0, y=170)


info_button = Button(root, text="HOW TO USE", height=3, width=20, command=infoShow)
info_button.place(relx=0.5, rely=0.80, anchor=CENTER)

# If several currencies will be added
currency = []
amount = []


def continue_adding():
    currency_toIn = Combo.current()
    if currency_toIn in currency:
        index = currency.index(currency_toIn)
        print("Already in")
        if len(en2.get()) == 0:
            print("sa")
        else:
            sum = int(en2.get()) + amount[index]
            amount[index] = sum;
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


# Add Button
add_btn = Button(root, text='ADD', height=3, width=20, command=continue_adding)
add_btn.place(relx=0.5, rely=0.50, anchor=CENTER)

new_currency = []


def open_Shares_Page():
    shares_page = Toplevel(root)
    shares_page.title("Split Portfolio")
    shares_page.geometry("800x400")
    shares_page.resizable(width=False, height=False)
    new_currency = transform(currency)
    print(new_currency)

    header_name = Label(shares_page, text="Name", bg="white", width=15, font="Verdana 8 bold")
    header_name.place(x=0, y=0)

    header_rank = Label(shares_page, text="Rank", bg="silver", width=10, font="Verdana 8 bold")
    header_rank.place(x=120, y=0)

    header_current_price = Label(shares_page, text="Current Price", bg="white", width=13, font="Verdana 8 bold")
    header_current_price.place(x=205, y=0)

    header_1_hr_change = Label(shares_page, text="1 HR Change", bg="silver", width=12, font="Verdana 8 bold")
    header_1_hr_change.place(x=315, y=0)

    header_24_hr_change = Label(shares_page, text="24 HR Change", bg="white", width=12, font="Verdana 8 bold")
    header_24_hr_change.place(x=410, y=0)

    header_7_day_change = Label(shares_page, text="7 Day Change", bg="silver", width=12, font="Verdana 8 bold")
    header_7_day_change.place(x=510, y=0)

    header_amount = Label(shares_page, text="Amount", bg="white", width=10, font="Verdana 8 bold")
    header_amount.place(x=610, y=0)

    header_current_value = Label(shares_page, text="Current Value", bg="silver", width=13, font="Verdana 8 bold")
    header_current_value.place(x=690, y=0)

    symbolstr = ','.join(('BTC,ETH,BNB,XRP,USDT,ADA,DOT,UNI,LTC,LINK,SHIB,XLM,BCH',
                          'THETA,FIL,USDC,TRX,DOGE,WBTC,VET,SOL,KLAY,EOS,XMR,LUNA',
                          'MIOTA,BTT,CRO,BUSD,FTT,AAVE,BSV,XTZ,ATOM,NEO,AVAX,ALGO',
                          'CAKE,HT,EGLD,XEM,KSM,BTCB,DAI,HOT,CHZ,DASH,HBAR,RUNE,MKR,ZEC',
                          'ENJ,DCR,MKR,ETC,GRT,COMP,STX,NEAR,SNX,ZIL,BAT,LEO,SUSHI',
                          'MATIC,BTG,NEXO,TFUEL,ZRX,UST,CEL,MANA,YFI,UMA,WAVES,RVN',
                          'ONT,ICX,QTUM,ONE,KCS,OMG,FLOW,OKB,BNT,HNT,SC,DGB,RSR,DENT',
                          'ANKR,REV,NPXS,VGX,FTM,CHSB,REN,IOST,BTMX,CELO,PAX,CFX'))

    symbol_list = symbolstr.split(',')
    key = os.environ.get('')

    url = f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    print(url)
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '05c3873e-16e1-4a7c-8b31-3947cce36f62'
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
    column_count_value = 19.50
    for i in new_currency:
        x = 0

        current_value = float(amount[count]) * float(data[i]['quote']['USD']['price'])

        name = Label(shares_page, text=data[i]['name'], bg="white", width=16)
        name.place(x=0, y=column_count_value)

        rank = Label(shares_page, text=data[i]['cmc_rank'], width=12, bg="silver")
        rank.place(x=120, y=column_count_value)

        current_price = Label(shares_page, text="${0:.2f}".format(float(data[i]['quote']['USD']['price'])), width=15,
                              bg="white", )
        current_price.place(x=205, y=column_count_value)

        one_hr_change = Label(shares_page, text="{0:.2f}%".format(float(data[i]['quote']['USD']['percent_change_1h'])),
                              bg="silver", width=13,
                              fg=red_green(float(data[i]['quote']['USD']["percent_change_1h"])))
        one_hr_change.place(x=315, y=column_count_value)

        tf_hr_change = Label(shares_page, text="{0:.2f}%".format(float(data[i]['quote']['USD']['percent_change_24h'])),
                             bg="white", width=14,
                             fg=red_green(float(data[i]['quote']['USD']["percent_change_24h"])))
        tf_hr_change.place(x=410, y=column_count_value)

        seven_day_change = Label(shares_page,
                                 text="{0:.2f}%".format(float(data[i]['quote']['USD']['percent_change_7d'])),
                                 bg="silver", width=15,
                                 fg=red_green(float(data[i]['quote']['USD']["percent_change_7d"])))
        seven_day_change.place(x=510, y=column_count_value)

        amount_value = Label(shares_page, text="{0:.2f}".format(amount[count]), width=14, bg="white")
        amount_value.place(x=610, y=column_count_value)

        current_value = Label(shares_page, text="${0:.2f}".format(float(current_value)), width=15, bg="silver")
        current_value.place(x=690, y=column_count_value)

        column_count_value += 20
        row_count += 1
        count += 1

        # Creating dataset
        def showpi():

            plt.pie(amount, labels=new_currency, autopct='%1.1f%%')
            plt.show()

        pie_button = Button(shares_page, text="Pie Chart", command=showpi)
        pie_button.place(x=360, y=365)

        def showFuturePrice():
            global futurePrice
            futurePanel = Toplevel(root)
            futurePanel.title("Estimated Future Price")
            futurePanel.geometry("400x400")
            futurePanel.resizable(width=False, height=False)
            hss = Label(futurePanel, text="Estimated Future Prices", bg="silver", width=50, font="Verdana 8 bold")
            hss.grid(row=0, column=0, sticky=N + S + E + W)

            fp_name = Label(futurePanel, text="Name", bg="white", width=10, font="Verdana 8 bold")
            fp_name.place(x=0, y=35)

            fp_future = Label(futurePanel, text="Estimated Future Price", bg="silver", width=20, font="Verdana 8 bold")
            fp_future.place(x=80, y=35)

            fp_current = Label(futurePanel, text="Current Price ", bg="white", width=20, font="Verdana 8 bold")
            fp_current.place(x=240, y=35)

            column_count_future = 60
            for i in new_currency:
                futurePrice = float(data[i]['quote']['USD']['price']) + (float(data[i]['quote']['USD']['price']) * ((
                        float(data[i]['quote']['USD']['percent_change_7d']) + float(
                    data[i]['quote']['USD']["percent_change_24h"]))/2))
                if futurePrice < 0:
                    futurePrice = 0

                future_price_button_name = Label(futurePanel, text=data[i]['name'], width=10, bg="white")
                future_price_button_name.place(x=0, y=column_count_future)

                future_price_button_price = Label(futurePanel, text="${0:.2f}".format(float(futurePrice)), width=20,
                                                  bg="silver", font="Verdana 8 bold")
                future_price_button_price.place(x=80, y=column_count_future)

                price_button_price = Label(futurePanel, text="${0:.2f}".format(float(data[i]['quote']['USD']['price'])),
                                           width=20, bg="white", font="Verdana 8 bold")
                price_button_price.place(x=240, y=column_count_future)
                column_count_future += 20


    def get_market_chart(coin_id, vs_currency='usd', days='max', interval='daily'):

        url = f'https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart'
        payload = {'vs_currency': vs_currency, 'days': days, 'interval': interval}
        response = requests.get(url, params=payload)
        data = response.json()

        timestamp_list, price_list = [], []

        for price in data['prices']:
            timestamp_list.append(datetime.datetime.fromtimestamp(price[0] / 1000))
            price_list.append(price[1])
        raw_data = {
            'timestamp': timestamp_list,
            'price': price_list
        }
        df = pd.DataFrame(raw_data)
        return df

    history_combo = ["BTC", "ETH", "BNB", "XRP", "DOGE", "DOT", "LTC", "SHIB", "SOL", "ADA"]

    future_price_button = Button(shares_page, text="Estimated Future Price", command=showFuturePrice)
    future_price_button.place(x=15, y=365)

    # for i in history_combo:
    # if

    def showNews(event=None):
        webview.create_window('Coin News', 'https://coinmarketcap.com/headlines/news/')
        webview.start()

    showsNews_button = Button(shares_page, text="Show News", command=showNews)
    showsNews_button.place(x=210, y=365)

    def don(event=None):
        shares_page.destroy()
        open_Shares_Page()

    def hist_data(event=None):
        x = ''
        if Comboy.current() == 0:
            x += 'bitcoin'
        if Comboy.current() == 1:
            x = 'ethereum'
        if Comboy.current() == 2:
            x = 'binancecoin'
        if Comboy.current() == 3:
            x = 'ripple'
        if Comboy.current() == 4:
            x = 'dogecoin'
        if Comboy.current() == 5:
            x = 'polkadot'
        if Comboy.current() == 6:
            x = 'litecoin'
        if Comboy.current() == 7:
            x = 'shiba-inu'
        if Comboy.current() == 8:
            x = 'solana'
        if Comboy.current() == 9:
            x = 'cardano'
        market_info = get_market_chart(x, 'usd', '30')
        market_info.plot(y='price', x='timestamp', color='#4285F4')
        plt.show()

    Comboy = ttk.Combobox(shares_page, state="readonly", width=10, values=history_combo)
    Comboy.set("BTC")
    Comboy.place(x=130, y=335)

    showHist = Button(shares_page, text="Coin Price History", command=hist_data)
    showHist.place(x=15, y=334)

    update_button = Button(shares_page, text="Update Prices", command=don)
    update_button.place(x=480, y=365)

    def don2(event=None):
        count = 0
        xx = Comboc.current()
        column_count_value2 = 419.50
        for i in new_currency:
            if xx == 0:
                values = float(data[i]['quote']['USD']['price'])
                current_price = Label(shares_page, text="$ {0:.2f}".format(values),
                                      width=15,
                                      bg="white", )
                current_price.place(x=205, y=column_count_value2)
                current_value = Label(shares_page, text="$ {0:.2f}".format(float(amount[count]) * values), width=15,
                                      bg="silver")
                current_value.place(x=690, y=column_count_value2)
            if xx == 1:
                values = float(data[i]['quote']['USD']['price'])
                current_price = Label(shares_page,
                                      text="€ {0:.2f}".format(float(data[i]['quote']['USD']['price']) * 0.97),
                                      width=15,
                                      bg="white", )
                current_price.place(x=205, y=column_count_value2)
                current_value = Label(shares_page, text="€ {0:.2f}".format(float(amount[count]) * values * 0.97),
                                      width=15, bg="silver")
                current_value.place(x=690, y=column_count_value2)
            if xx == 2:
                values = float(data[i]['quote']['USD']['price'])
                current_price = Label(shares_page,
                                      text="₺ {0:.2f}".format(float(data[i]['quote']['USD']['price']) * 18.67),
                                      width=15,
                                      bg="white", )
                current_price.place(x=205, y=column_count_value2)
                current_value = Label(shares_page, text="₺ {0:.2f}".format(float(amount[count]) * values * 18.67),
                                      width=15, bg="silver")
                current_value.place(x=690, y=column_count_value2)
            if xx == 3:
                values = float(data[i]['quote']['USD']['price'])
                current_price = Label(shares_page,
                                      text="£ {0:.2f}".format(values * 0.83),
                                      width=15,
                                      bg="white", )
                current_price.place(x=205, y=column_count_value2)
                current_value = Label(shares_page, text="£ {0:.2f}".format((float(amount[count]) * values * 0.83)),
                                      width=15, bg="silver")
                current_value.place(x=690, y=column_count_value2)
            column_count_value2 += 20
            count += 1

    currList = ["USD", "EUR", "TRY", "GBP"]
    Comboc = ttk.Combobox(shares_page, state="readonly", width=5, values=currList)
    Comboc.set("USD")
    Comboc.place(x=620, y=368)

    update_curr = Button(shares_page, text="Change Currency", command=don2)
    update_curr.place(x=680, y=365)


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
