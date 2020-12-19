from grandpy.parser import Parser

parser = Parser()

# lowercase
def test_to_lowercase():
    """ """
    result_a = parser.lowercase("jklMnOpQrsTu")
    result_b = parser.lowercase("Monsieur et Madame TrucMuche")
    assert result_a == "jklmnopqrstu"
    assert result_b == "monsieur et madame trucmuche"

# punctuation
def test_remove_punctuations():
    """ I remove all the punctuation. """
    result_a = parser.punctuation("hop,hop, hop, zut: ça v;a plus! ..../_ super...")
    result_b = parser.punctuation("(c'est... top) #& par-ce === que j'ai-- \{réussi] à fa}ire( nimp)")
    result_c = parser.punctuation(";.,:!?=()[]{}\/")
    assert result_a == "hop hop hop zut ça va plus super"
    assert result_b == "c est top parce que j ai réussi à faire nimp"
    assert result_c == " "

# tokenization
def test_tokenization():
    """ """
    result_a = parser.tokenization("hop hop hop zut ça va plus super")
    result_b = parser.tokenization("c est top parce que j ai réussi à faire nimp")
    assert result_a == ['hop', 'hop', 'hop', 'zut', 'ça', 'va', 'plus', 'super']
    assert result_b == ['est', 'top', 'parce', 'que', 'ai', 'réussi', 'faire', 'nimp']

#stop words
def test_remove_stop_words():
    """ """
    result_a = parser.remove_stopwords(['vives', 'toujours', 'puisque', 'orléans', 'pure', '16', 'camille'])
    assert result_a == ['orléans', '16', 'camille']

# class test
def test_parser():
    result_a = parser.parser("je cherche l'adresse de la maison de la radio à paris ou à marseille")
    # assert result_a == ['cherche', 'adresse', 'maison', 'radio', 'paris', 'marseille']
    assert result_a == "cherche adresse maison radio paris marseille"




# # spacing
# def test_remove_spacing():
#     pass

# # accents
# def test_remove_accents():
#     pass