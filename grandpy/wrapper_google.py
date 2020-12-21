import requests
from config import GURL, GKEY, UAGENT


class WrapperGoogle:
    """ """

    def __init__(self):
        self.URL = GURL
        self.HEADERS = {"User-Agent": UAGENT}
        self.PARAMS = {
            "key": GKEY
        }

    def connection(self):
        try:
            connection = requests.get(
                url=self.URL, 
                params=self.PARAMS, 
                headers=self.HEADERS
            )
            return connection

        except requests.RequestException as exception:
            print(exception)

    def request(self, query):
        pass

if __name__ == "__main__":
    wgoogle = WrapperGoogle()

    print(wgoogle.connection(), type(wgoogle.connection()))