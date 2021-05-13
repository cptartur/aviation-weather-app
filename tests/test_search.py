from avw.search import search_airport


def test_search_airport(client):
    res = search_airport('EPKK')
    assert type(res) == list
    assert len(res) > 0
    assert any(r['_source']['ident'] == 'EPKK' for r in res)

    res = search_airport('Kraków')
    assert type(res) == list
    assert len(res) > 0
    assert any(r['_source']['ident'] == 'EPKK' for r in res)

    res = search_airport('John Paul')
    assert type(res) == list
    assert len(res) > 0
    assert any(r['_source']['ident'] == 'EPKK' for r in res)


def test_search_invalid_airport(client):
    assert search_airport('XXXX') is None


def test_search_invalid_input(client):
    assert search_airport(231123) is None
    assert search_airport(None) is None
    assert search_airport('') is None
    assert search_airport('231123') is None
    assert search_airport([]) is None
    assert search_airport({}) is None
