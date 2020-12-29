
from gp_parser import GPParser
from wrapper_google import WrapperGoogle
from wrapper_wiki import WrapperWiki

class GrandPy:
    """ """

    def __init__(self):
        """ """
        self.gpparser = GPParser()
        self.wgoogle = WrapperGoogle()
        self.wwiki = WrapperWiki()

    def main_coord(self, query):
        """ """
        response = {}
        response["query"] = query

        # Parsing
        parsing_result = self.gpparser.parser(query)
        if parsing_result == "wiki":
            response["flow"] = False
            return response
        response["parsing"] = parsing_result

        # Google Search
        google_result = self.wgoogle.request(parsing_result)
        # google_nbe_result = self.wgoogle.number_of_results(google_result)
        # print("\n== Le nombre de résultat de la recherche Google : ", google_nbe_result, "==")
        if google_result == None:
            response["flow"] = False
            return response
        place_result = self.wgoogle.informations(google_result)
        print("\n== Les informations sur le lieu : ", place_result, "==")
        location_result = self.wgoogle.coordinates(google_result)
        print("\n== La location Google : ", location_result, "==")
        
        
        
        
        
        coord_result = self.wwiki.location_to_coord(location_result)
        print("\n== coordonnées à passer à Wikipedia : ", coord_result, "==")
        pageid_result = self.wwiki.coord_to_pageid(coord_result)
        if not pageid_result:
            print("Désolé, je n'ai rien à dire...")
            return
        print("\n== L'ID de la page wikipedia : ", pageid_result, "==")
        text_result = self.wwiki.wiki_text(str(pageid_result))
        print("\n== Le texte : ", text_result, "==")
        return response


if __name__ == "__main__":
    grandpy = GrandPy()

    # print(grandpy.main_coord('thiais mairie'))
    print(grandpy.main_coord('zapzapzapzap'))
    # grandpy.main_name()
