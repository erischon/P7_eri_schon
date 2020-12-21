from grandpy.wrapper_google import WrapperGoogle

wgoogle = WrapperGoogle()

def test_google_request():
    result_a = str(type(wgoogle.request()))
    assert result_a == "<class 'dict'>"

# def test_answer_to_resquest():
#     pass

# def test_format_of_answer():
#     pass