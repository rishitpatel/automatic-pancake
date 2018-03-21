from bs4 import BeautifulSoup as bsoup
from urllib import request as req
url = 'https://finance.yahoo.com/quote/AAPL?p=AAPL'
url_acc = req(url)
url_acc = req.urlopen(url)
url_html = url_acc.read()
url_acc.close()
url_soup = bsoup(url_html, "html.parser")


containers = url_soup.findAll("div", {"id": "quote-header-info"})
len(containers)


stock_name = containers[0].findAll("h1", {"data-reactid": "7"})
stock_name[0].text
stock_name[0].text.strip()
stock_name[0].text.strip(''')