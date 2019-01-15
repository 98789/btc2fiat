import sqlite3
from datetime import datetime as dt

import requests
from bs4 import BeautifulSoup as bs


def format_date(date, format):
    '''
    format a date
    '''

    try:
        return dt.strptime(date, '%Y%m%d').strftime(format)
    except ValueError:
        raise ValueError('Date format must be yyyymmdd')


def get_coindesk(btc, date):
    '''
    get_price using coindesk data
    '''

    date = format_date(date, '%Y-%m-%d')

    url = ('https://api.coindesk.com/v1/bpi/historical/'
          'close.json?start={date}&end={date}'.format(date=date))

    r = requests.get(url)
    value = r.json()['bpi'][date]

    return value * btc


def get_coinmarketcap(btc, date):
    '''
    get_price using coinmarketcap data
    '''

    url = ('https://coinmarketcap.com/currencies/bitcoin/'
          'historical-data/?start={date}&end={date}'.format(
           date=date))

    r = requests.get(url)
    soup = bs(r.text, 'html.parser')

    val_tag = soup.find('tbody').find_all('td')[4]
    value = float(val_tag.text)

    return value * btc


def get_value(btc, date, src='coindesk'):
    '''
    get how much in USD some btc was worth at a given date,
    using data from the specified source.
    '''

    sources = {'coindesk': get_coindesk,
        'coinmarketcap': get_coinmarketcap
    }

    source = sources.get(src, get_coindesk)
    value = source(btc, date)

    return value