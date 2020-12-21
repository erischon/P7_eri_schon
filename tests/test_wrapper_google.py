from grandpy.wrapper_google import WrapperGoogle

wgoogle = WrapperGoogle()

def test_google_api_connection():
    result_a = wgoogle.connection()
    assert result_a == "je veux une fonction"

# def test_answer_to_resquest():
#     pass

# def test_format_of_answer():
#     pass