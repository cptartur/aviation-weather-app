from avw.search import search_airport
from flask import session


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


def test_session(client):
    client.get('/')
    assert 'recent_apts' not in session

    client.get('/search/EPKK', follow_redirects=True)
    assert 'recent_apts' in session
    assert 'EPKK' in session['recent_apts'] 
    assert session['recent_apts'][0] == 'EPKK'

    client.get('/search/KSFO')
    client.get('/search/EPGD')
    client.get('/search/EPWA')
    client.get('/search/EDDH')
    assert {'KSFO', 'EPGD', 'EPWA', 'EDDH'}.issubset(session['recent_apts'])
    assert 'EPKK' in session['recent_apts'] 
    
    client.get('/search/KLAX')
    assert len(session['recent_apts']) == 5
    assert 'KLAX' in session['recent_apts'] 
    assert {'KSFO', 'EPGD', 'EPWA', 'EDDH'}.issubset(session['recent_apts'])
    assert 'EPKK' not in session['recent_apts']
