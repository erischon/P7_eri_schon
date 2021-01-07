from grandpy.wrapper_google import WrapperGoogle

wgoogle = WrapperGoogle()

google_result = [{
    'formatted_address': '94320 Thiais, France', 
    'geometry': {'location': {'lat': 48.760344, 'lng': 2.387405}, 
    'viewport': {'northeast': {'lat': 48.774788, 'lng': 2.4060011}, 'southwest': {'lat': 48.7461089, 'lng': 2.36777}}}, 
    'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/geocode-71.png', 'name': 'Thiais', 
    'photos': [{
        'height': 1836, 
        'html_attributions': ['<a href="https://maps.google.com/maps/contrib/101801343764266728981">Farid b.</a>'], 
        'photo_reference': 'ATtYBwJNoduVb3yUlD0DvJz0s0pkxGrdK7yzjnGVPQAKs0V6BQuQLIEkEBeAZBZNbe_15dACJlszlVhNOhWAy4xyT3YmGP-c8jkzIjOCtiv6NMrb2GBxbI8BGX8M5z9OFvoQ-2SA30orQ1qaoQ8ua3eA5zZb5AHTYANEnXzvJ1bUp6aSFvQq', 
        'width': 3264
        }], 
    'place_id': 'ChIJ1fhlHWx05kcRsDeLaMOCCwQ', 
    'reference': 'ChIJ1fhlHWx05kcRsDeLaMOCCwQ', 'types': ['locality', 'political']
    }]

def mock_wgoogle_request(*args, **kwargs):
    return google_result

result = mock_wgoogle_request()


def test_google_request():
    """ I test if there is a answer to a request. """
    result_a = str(type(mock_wgoogle_request()))
    assert result_a == "<class 'list'>"

def test_number_of_results():
    """ I test if I have a number. """
    result_a = str(type(wgoogle.number_of_results(result)))
    assert result_a == "<class 'int'>"

def test_coordinates():
    """ I test if the answer is a dictionary. """
    result_a = str(type(wgoogle.coordinates(result)))
    assert result_a == "<class 'dict'>"

def test_informations():
    """ I test if the answer is a dictionary. """
    result_a = str(type(wgoogle.informations(result)))
    assert result_a == "<class 'dict'>"
