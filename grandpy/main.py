
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
        google_result = self.wgoogle.request(text_result)
        place_result = self.wgoogle.informations(google_result)
        print(place_result)
        location_result = self.wgoogle.coordinates(google_result)
        coord_result = self.wwiki.location_to_coord(location_result)
        pageid_result = self.wwiki.coord_to_pageid(coord_result)
        text_result = self.wwiki.wiki_text(pageid_result)
        print(text_result)




if __name__ == "__main__":
    grandpy = GrandPy()

    grandpy.main()
