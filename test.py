import datetime
import time
from coins.threads import PriceUpdateThread
from coins import db
from coins.models import Price
from coins import settings


def monitor(interval):
    session = db.Session()
    last = datetime.datetime.now()
    while True:
        prices = session.query(Price).filter(Price.time > last).order_by(Price.time).all()
        print('MONITORING ({}):'.format(datetime.datetime.now().strftime(settings.DATETIME_FORMAT)))
        for price in prices:
            print(price)
        if not prices:
            print('nothing')
        last = datetime.datetime.now()
        time.sleep(interval)


prices_thread = PriceUpdateThread(2)
prices_thread.start()
monitor(5)
