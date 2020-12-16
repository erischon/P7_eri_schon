from grandpy.parser import Parser

parser = Parser()

# lowercase
def test_to_lowercase():
    result_a = parser.lowercase("jklMnOpQrsTu")
    result_b = parser.lowercase("Monsieur et Madame TrucMuche")
    assert result_a == "jklmnopqrstu"
    assert result_b == "monsieur et madame trucmuche"

# punctuation
def test_remove_punctuations():
    result_a = parser.punctuation("hop,hop, hop, zut: ça v;a plus! ..../_ super...")
    result_b = parser.punctuation("(c'est... top) #& par-ce === que j'ai-- \{réussi] à fa}ire( nimp)")
    result_c = parser.punctuation(";.,:!?=()[]{}\/")
    assert result_a == "hop hop hop zut ça va plus super"
    assert result_b == "c est top parce que j ai réussi à faire nimp"
    assert result_c == " "

# # spacing
# def test_remove_spacing():
#     pass

# # accents
# def test_remove_accents():
#     pass

# # stopwords
# def test_remove_stopwords():
#     pass

# # class test
# def clean_text():
#     pass