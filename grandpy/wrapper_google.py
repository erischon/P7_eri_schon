import requests
from .config import GURL, GKEY, UAGENT


class WrapperGoogle:
    """ """

    def __init__(self):
        self.URL = GURL
        self.HEADERS = {"User-Agent": UAGENT}
        self.GKEY = GKEY
        self.PARAMS = {"key": GKEY}

    def request(self, query="mairie thiais"):
        """ I make the request to google place. """
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
            return results["results"]

        except requests.RequestException as exception:
            print(exception)

    def number_of_results(self, results):
        """ I check the number of results. """
        return len(results)

    def coordinates(self, results):
        """ I retrieve the coordinates of the place. """
        result = {
            "geometry": results[0].get('geometry')
        }
        return result

    def informations(self, results):
        """ I retrieve the informations of the place. """
        result = {
            "name": results[0].get('name'),
            "formatted_address": results[0].get('formatted_address'),
            "types": results[0].get('types')
        }
        return result


if __name__ == "__main__":
    wgoogle = WrapperGoogle()

    # print(wgoogle.request(), type(wgoogle.request()))
    # print(wgoogle.number_of_results(wgoogle.request()))
    # print(wgoogle.coordinates(wgoogle.request()))
    # print(wgoogle.informations(wgoogle.request()))