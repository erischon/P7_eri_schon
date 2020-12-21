import requests
from config import *


class WrapperGoogle:
    """ """

    def __init__(self):
        self.url = "https://maps.googleapis.com/maps/api/geocode/json"
        self.params = {
            "key": GKEY
        }

    def connection(self):
        try:
            print(self.params["key"])

        except:
            pass

if __name__ == "__main__":
    wgoogle = WrapperGoogle()

    print(wgoogle.connection())