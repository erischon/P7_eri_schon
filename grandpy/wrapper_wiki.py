import requests

from config import Config


class WrapperWiki:
    """ """

    def __init__(self):
        """ """
        config = Config()
        self.URL = config.WURL

    def location_to_coord(self, location):
        """ """
        return f"{location.get('location').get('lat')}|{location.get('location').get('lng')}"

    def coord_to_pageid(self, coord="48.76569917989272|2.392394129892722"):
        """ """
        try:
            request = requests.get(
                url = self.URL, 
                params = {
                    "action": "query",
                    "list": "geosearch",
                    "gscoord": coord,
                    "gsradius": 100,
                    "gslimit": 1,
                    "format": "json",
                },
            )
            results = request.json()
            # results_a = results.get('query').get('geosearch')
            print(results, type(results))

            if len(results.get('query').get('geosearch')) < 1:
                print("Désolé, je n'ai rien à dire")
            else:
                result = results.get('query').get('geosearch')
                result = result[0].get('pageid')
                return result

        except requests.RequestException as exception:
            print(exception)

    def wiki_text(self, pageid="1509079"):
        """ """
        try:
            request = requests.get(
                url = self.URL, 
                params = {
                    "action": "query",
                    "prop": "extracts",
                    "exsentences": 3,
                    "exlimit": 1,
                    "pageids": pageid,
                    "explaintext": 1,
                    "formatversion": 1,
                    "format": "json",
                },
            )
            results = request.json()

            if len(results) < 1:
                print("Désolé, je n'ai rien à dire")
            else:
                result = results.get('query').get('pages').get(pageid).get('extract')
                return result

        except requests.RequestException as exception:
            print(exception)
    

if __name__ == "__main__":
    wwiki = WrapperWiki()

    # print(wwiki.location_to_coord({'location': {'lat': 48.76569917989272, 'lng': 2.392394129892722}}), type(wwiki.location_to_coord({'location': {'lat': 48.76569917989272, 'lng': 2.392394129892722}})))
    print(wwiki.coord_to_pageid("48.76569917989272|2.392394129892722"), type(wwiki.coord_to_pageid("48.76569917989272|2.392394129892722")))
    # print(wwiki.coord_to_pageid("46.2425288|6.067658499999999"), type(wwiki.coord_to_pageid("48.46.2425288|6.067658499999999")))



    # print(wwiki.wiki_text("5548980"))
    # print(wwiki.name_to_pageid("mairie_de_thiais"))