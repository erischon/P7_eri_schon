import requests

from .config import Config


class WrapperGoogle:
    """ """

    def __init__(self):
        """ """
        config = Config()
        self.URL = config.GURL
        self.HEADERS = {"User-Agent": config.UAGENT}
        self.GKEY = config.GKEY
        self.PARAMS = {"key": config.GKEY}

    def request(self, query="thiais"):
        """ I make the request to google place. """
        try:
            request = requests.get(
                url = self.URL, 
                params = {
                    "key": self.GKEY,
                    "query": query
                }, 
                headers = self.HEADERS
            )
            results = request.json()
            
            if results.get('status') != 'OK':
                # print("Désolé, je n'ai trouvé aucun lieu qui correspond à cette recherche.")
                results = None
                return results
            else:
                return results["results"]

        except requests.RequestException as exception:
            print(exception)

    def number_of_results(self, results):
        """ I check the number of results. """
        return len(results)

    def coordinates(self, results):
        """ I retrieve the coordinates of the place. 
        exemple :
        """
        result = {
            "location": results[0].get('geometry').get('viewport').get('northeast')
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

    # def result_name(self, results):
    #     """ """
    #     result = results[0].get('name')
    #     result = result.replace(" ", "_")
    #     return result   


if __name__ == "__main__":
    wgoogle = WrapperGoogle()

    print(wgoogle.request("mairie thiais wiki"), type(wgoogle.request()))
    # print(wgoogle.request("moutarde dijon paris wiki"), type(wgoogle.request()))
    # print(wgoogle.request("chaussures tombouktou besoin marcher aller himalaya"), type(wgoogle.request()))
    # print(wgoogle.number_of_results(wgoogle.request()))
    # print(wgoogle.coordinates(wgoogle.request()))
    # print(wgoogle.informations(wgoogle.request()))
    # print(wgoogle.result_name(wgoogle.request()))