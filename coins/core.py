import re
import requests
from bs4 import BeautifulSoup
from . import db
from .models import Metal, Price


def get_stooq_price(name):
    name = name.lower()
    url = 'https://stooq.pl/q/?s=' + name
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    search_phrase = 'aq_{name}_c[0-9]'.format(name=name)
    tag = soup.find('span', id=re.compile(search_phrase))
    if tag is None:
        return None
    else:
        try:
            return float(tag.get_text())
        except ValueError:
            return None


def update_metal_prices():
    session = db.get_session()
    metals = session.query(Metal).all()
    for metal in metals:
        value = get_stooq_price(metal.symbol)
        if value is not None:
            price = Price(metal=metal, value=value)
            session.add(price)
            session.commit()
