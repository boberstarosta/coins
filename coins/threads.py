import time
from threading import Thread
from .core import update_metal_prices


class PriceUpdateThread(Thread):
    def __init__(self, interval=30):
        """
        :param interval: int interval between price checks in seconds
        """
        super().__init__(daemon=True)
        self.interval = interval

    def run(self):
        while True:
            update_metal_prices()
            time.sleep(self.interval)
