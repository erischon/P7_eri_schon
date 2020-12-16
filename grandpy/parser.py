import re

class Parser:
    """ """

    def __init__(self):
        pass

    def lowercase(self, value):
        """ I lowercase the text. """
        return value.lower()

    def punctuation(self, value):
        """ I remove the punctuations. """
        value = re.sub(r'_', '', value)
        value = re.sub(r',', ' ', value)
        value = re.sub(r'\'', ' ', value)
        value = re.sub(r'[^\w\s]','', value)
        value = re.sub('\s+',' ',value)
        return value

if __name__ == "__main__":
    parser = Parser()
    
    # === Tests of methods ===
    # print(parser.lowercase("ToTO"))
    # print(parser.punctuation("hop,hop, hop, zut: ça v;a plus! ..../_ super..."))