import re
import nltk
from nltk.stem.snowball import FrenchStemmer

class Parser:
    """ """

    def __init__(self):
        self.stemmer = FrenchStemmer()

    def lowercase(self, value):
        """ I lowercase the text. """
        return value.lower()

    def punctuation(self, value):
        """ I remove the punctuations. """
        value = re.sub('_', ' ', value)
        value = re.sub(',', ' ', value)
        value = re.sub('\'', ' ', value)
        value = re.sub(r'[^\w\s]','', value)
        value = re.sub(r'\s+',' ',value)
        return value

    def tokenization(self, value):
        """ """
        value = nltk.word_tokenize(value)
        return value



if __name__ == "__main__":
    parser = Parser()
    
    # === Tests of methods ===
    # print(parser.lowercase("ToTO"))
    # print(parser.punctuation("hop,hop, hop, zut: ça v;a plus! ..../_ super..."))
    print(parser.tokenization("hop hop hop zut ça va plus super"))