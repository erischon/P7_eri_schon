from grandpy.main import GrandPy

gp = GrandPy()

result = 'mairie de thiais'

def test_main():
    """ """
    result_a = str(type(gp.main(result)))
    assert result_a == "<class 'dict'>"