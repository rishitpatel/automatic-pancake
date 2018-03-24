from bs4 import BeautifulSoup as bsoup
from urllib import request as req
from datetime import datetime
import pandas as pd

quote_list = ['AAPL','FB','SPY','NVDA','AMZN','BAC','NFLX','BABA','MU','CSCO']

symbols = []
stocks_names = []
prices = []

for quote in quote_list:

    url = 'https://finance.yahoo.com/quote/' + quote +'?p=' + quote
    url_acc = req.urlopen(url)
    url_html = url_acc.read()
    url_acc.close()
    url_soup = bsoup(url_html, "html.parser")


    containers = url_soup.findAll("div", {"id": "quote-header-info"})
    #print(len(containers))


    stock_name = containers[0].findAll("h1", {"data-reactid": "7"})
    stock_name = stock_name[0].text
    #print (stock_name)
    stock_name_l = stock_name.split('-')
    stock_sym = stock_name_l[0].strip()
    stock_company = stock_name_l[1].strip()
    #print (stock_name[0].text.strip())
    #print (containers)

    #print(stock_name_l)
    #print(stock_sym)
    #print(stock_company)

    stock_price = containers[0].findAll("span", {"data-reactid": "36"})
    #print (stock_price[0].text)

    symbols.append(stock_sym)
    stocks_names.append(stock_company)
    prices.append(stock_price)

data = pd.DataFrame({"symbol": symbols, "Comapany/ETF name": stocks_names, "Price": prices})
print(data)