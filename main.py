# топ10 криптовалют


import pandas as pd
import requests
from bs4 import BeautifulSoup

crypto_name_list = []
crypto_price_list = []
cryto_market_cap_list = []
cryto_circ_suply_list = []
cryto_symbol_list = []
date_list = []

df = pd.DataFrame()


def scrape(date='20151231/'):
    URL = 'https://coinmarketcap.com/historical/' + date
    webpage = requests.get(URL)
    soup = BeautifulSoup(webpage.text, 'html.parser')

    tr = soup.find_all('tr', attrs={'class': 'cmc-table-row'})
    count = 0
    for row in tr:
        if count == 17:
            break;
        count = count + 1
        name_column = row.find('td', attrs={
            'class': 'cmc-table__cell cmc-table__cell--sticky cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__name'})
        crypto_name = name_column.find('a', attrs={'cmc-table__column-name--name cmc-link'}).text.strip()
        cryto_market_cap = row.find('td', attrs={
            'class': 'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__market-cap'}).text.strip()
        crypto_price = row.find('td', attrs={
            'class': 'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__price'}).text.strip()
        cryto_circ_suply_symbol = row.find('td', attrs={
            'class': 'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__circulating-supply'}).text.strip()
        cryto_circ_suply = cryto_circ_suply_symbol.split(' ')[0]
        cryto_symbol = cryto_circ_suply_symbol.split(' ')[1]
        date1 = str(date)
        crypto_name_list.append(crypto_name)
        cryto_market_cap_list.append(cryto_market_cap)
        crypto_price_list.append(crypto_price)
        cryto_circ_suply_list.append(cryto_circ_suply)
        cryto_symbol_list.append(cryto_symbol)

        date_list.append(date1[0:4])


scrape(date='20151231/')

df['Name'] = crypto_name_list
df['Market Cap'] = cryto_market_cap_list
df['Price'] = crypto_price_list
df['Supply'] = cryto_circ_suply_list
df['Symbol'] = cryto_symbol_list
df['Date'] = date_list
df
