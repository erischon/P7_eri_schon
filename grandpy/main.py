
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

    def main(self):
        """ """
        result = input("un texte : ")
        text_result = self.gpparser.parser(result)
        print("Le texte parsé : ", text_result)
        google_result = self.wgoogle.request(text_result)
        print("Le résultat de la recherche Google : ", google_result)
        if google_result == None:
            print("Je ne trouve rien !")
            return
        place_result = self.wgoogle.informations(google_result)
        print("Les informations sur le lieu : ", place_result)
        location_result = self.wgoogle.coordinates(google_result)
        print("La location Google : ", location_result)
        coord_result = self.wwiki.location_to_coord(location_result)
        print("coordonnées à passer à Wikipedia : ", coord_result)
        pageid_result = self.wwiki.coord_to_pageid(coord_result)
        print("L'ID de la page wikipedia : ", pageid_result)
        text_result = self.wwiki.wiki_text(str(pageid_result))
        print("Le texte : ", text_result)




if __name__ == "__main__":
    grandpy = GrandPy()

    grandpy.main()
