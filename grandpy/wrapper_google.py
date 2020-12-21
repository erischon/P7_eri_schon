import requests
from config import GURL, GKEY, UAGENT


class WrapperGoogle:
    """ """

    def __init__(self):
        self.URL = GURL
        self.HEADERS = {"User-Agent": UAGENT}
        self.GKEY = GKEY
        self.PARAMS = {
            "key": GKEY
        }

    def request(self, query="paris"):
        try:
            request = requests.get(
                url = self.URL, 
                params = {
                    "key": GKEY,
                    "query": query
                }, 
                headers = self.HEADERS
            )
            results = request.json()
            return results

        except requests.RequestException as exception:
            print(exception)

    def coordinates(self, results):
        """ """
        request = self.connection(params={"query": query})
        print(request)


if __name__ == "__main__":
    wgoogle = WrapperGoogle()

    print(wgoogle.request(), type(wgoogle.request()))
    # print(wgoogle.request("paris"))