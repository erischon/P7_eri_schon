
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

    def main_coord(self):
        """ """
        result = input("\nQuel est ta recherche ? : ")
        text_result = self.gpparser.parser(result)
        print("\n== Le texte parsé : ", text_result, "==")
        google_result = self.wgoogle.request(text_result)
        google_nbe_result = self.wgoogle.number_of_results(google_result)
        print("\n== Le nombre de résultat de la recherche Google : ", google_nbe_result, "==")
        print("\n== Le résultat de la recherche Google : ", google_result, "==")
        if google_result == None:
            print("\n== Désolé, je ne trouve rien avec cette demande ! ==\n")
            return
        place_result = self.wgoogle.informations(google_result)
        print("\n== Les informations sur le lieu : ", place_result, "==")
        location_result = self.wgoogle.coordinates(google_result)
        print("\n== La location Google : ", location_result, "==")
        coord_result = self.wwiki.location_to_coord(location_result)
        print("\n== coordonnées à passer à Wikipedia : ", coord_result, "==")
        pageid_result = self.wwiki.coord_to_pageid(coord_result)
        print("\n== L'ID de la page wikipedia : ", pageid_result, "==")
        text_result = self.wwiki.wiki_text(str(pageid_result))
        print("\n== Le texte : ", text_result, "==")

    # def main_name(self):
    #     """ """
    #     result = input("\nQuel est ta recherche ? : ")
    #     text_result = self.gpparser.parser(result)
    #     print("\n== Le texte parsé : ", text_result, "==")
    #     google_result = self.wgoogle.request(text_result)
    #     google_nbe_result = self.wgoogle.number_of_results(google_result)
    #     print("\n== Le nombre de résultat de la recherche Google : ", google_nbe_result, "==")
    #     print("\n== Le résultat de la recherche Google : ", google_result, "==")
    #     if google_result == None:
    #         print("\n== Désolé, je ne trouve rien avec cette demande ! ==\n")
    #         return
    #     place_result = self.wgoogle.informations(google_result)
    #     print("\n== Les informations sur le lieu : ", place_result, "==")
    #     name_result = self.wgoogle.result_name(google_result)
    #     print("\n== Le nom trouvé : ", name_result, "==")
    #     # coord_result = self.wwiki.location_to_coord(location_result)
    #     # print("\n== coordonnées à passer à Wikipedia : ", coord_result, "==")
    #     pageid_result = self.wwiki.name_to_pageid(name_result)
    #     print("\n== L'ID de la page wikipedia : ", pageid_result, "==")
    #     text_result = self.wwiki.wiki_text(str(pageid_result))
    #     print("\n== Le texte : ", text_result, "==")


if __name__ == "__main__":
    grandpy = GrandPy()

    grandpy.main_coord()
    # grandpy.main_name()
