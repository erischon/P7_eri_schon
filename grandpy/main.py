
from .gp_parser import GPParser
from .wrapper_google import WrapperGoogle
from .wrapper_wiki import WrapperWiki

class GrandPy:
    """ """

    def __init__(self):
        """ """
        self.gpparser = GPParser()
        self.wgoogle = WrapperGoogle()
        self.wwiki = WrapperWiki()

    def main(self, query):
        """ I create the answer
        In: the query of the user
        Act: I create the answer
        Out: the result informations (dict)
        Out Ex: {
            'query': 'mairie de thiais', 
            'parsing': True, 
            'parsing_result': 'mairie thiais wiki', 
            'gresult': True, 
            'ginfos': {
                'name': 'Thiais', 
                'formatted_address': '94320 Thiais, France', 
                'types': ['locality', 'political']
                }, 
            'gcoord': {
                'location': {
                    'lat': 48.774788, 
                    'lng': 2.4060011
                    }
                }, 
            'wresult': True, 
            'wpageid': 13553086, 
            'wtext': 'Le cimetière nouveau de Vitry-sur-Seine est un des cimetières communaux de la commune de Vitry-sur-Seine, dans le département du Val-de-Marne.', 
            'wtitle': 'Cimetière nouveau de Vitry-sur-Seine'
        } 
        """
        response = {}
        response["query"] = query

        # Parsing
        parsing_result = self.gpparser.parser(query)
        if parsing_result == "wiki":
            response["parsing"] = False
            return response
        response["parsing"] = True
        response["parsing_result"] = parsing_result

        # Google Result
        google_result = self.wgoogle.request(parsing_result)

        if google_result == None:
            response["gresult"] = False
            return response
        response["gresult"] = True

        google_place_result = self.wgoogle.informations(google_result)
        response["ginfos"] = google_place_result

        google_location_result = self.wgoogle.coordinates(google_result)
        response["gcoord"] = google_location_result

        # Wiki result      
        coord_result = self.wwiki.location_to_coord(google_location_result)
        wiki_pageid_result = self.wwiki.coord_to_pageid(coord_result)
        if not wiki_pageid_result:
            response["wresult"] = False
            return response
        response["wresult"] = True
        response["wpageid"] = wiki_pageid_result

        wiki_text_result = self.wwiki.wiki_text(str(wiki_pageid_result))
        response["wtext"] = wiki_text_result.get("extract")
        response["wtitle"] = wiki_text_result.get("title")

        return response


if __name__ == "__main__":
    grandpy = GrandPy()

    # print(grandpy.main_coord('thiais mairie'))
    # print(grandpy.main('mairie de thiais'))
    # grandpy.main_name()
