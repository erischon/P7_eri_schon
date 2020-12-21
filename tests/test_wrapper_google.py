from grandpy.wrapper_google import WrapperGoogle

wgoogle = WrapperGoogle()
result = wgoogle.request()

def test_google_request():
    result_a = str(type(wgoogle.request()))
    assert result_a == "<class 'list'>"

def test_number_of_results():
    result_a = str(type(wgoogle.number_of_results(result)))
    assert result_a == "<class 'int'>"

def test_coordinates():
    result_a = str(type(wgoogle.coordinates(result)))
    assert result_a == "<class 'dict'>"

def test_informations():
    result_a = str(type(wgoogle.informations(result)))
    assert result_a == "<class 'dict'>"
