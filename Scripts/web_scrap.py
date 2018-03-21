from bs4 import BeautifulSoup as bsoup
from urllib import request as req
from datetime import datetime
url = 'https://finance.yahoo.com/quote/AAPL?p=AAPL'
url_acc = req.urlopen(url)
url_html = url_acc.read()
url_acc.close()
url_soup = bsoup(url_html, "html.parser")


containers = url_soup.findAll("div", {"id": "quote-header-info"})
#print(len(containers))


stock_name = containers[0].findAll("h1", {"data-reactid": "7"})
stock_name = stock_name[0].text
print (stock_name)
stock_name_l = stock_name.split('-')
stock_sym = stock_name_l[0].strip()
stock_company = stock_name_l[1].strip()
#print (stock_name[0].text.strip())
#print (containers)

print(stock_name_l)
print(stock_sym)
print(stock_company)

stock_price = containers[0].findAll("span", {"data-reactid": "14"})
print (stock_price[0].text)
