from flask import current_app
from elasticsearch import TransportError


def search_airport(name) -> list:
    if getattr(current_app, 'elasticsearch', None) is None:
        return None
    try:
        q: dict = current_app.elasticsearch.search(
            index=current_app.config['SEARCH_INDEX_NAME'],
            body={
                'query': {
                    'bool': {
                        'must': [
                            {
                                'multi_match': {
                                    'query': name,
                                    'type': 'phrase_prefix',
                                    'fields': ['ident', 'name', 'municipality'],
                                }
                            }
                        ],
                        'filter': [
                            {
                                'terms': {'type': ['large_airport', 'medium_airport']}
                            }
                        ]
                    }
                }
            }
        )
    except TransportError:
        return None
    if q['timed_out'] is False and q['hits']['total']['value'] > 0:
        return sorted(q['hits']['hits'], key=lambda k: k['_score'], reverse=True)
    else:
        return None


def get_airport_name(code: str) -> str:
    if getattr(current_app, 'elasticsearch', None) is None:
        return None
    try:
        q: dict = current_app.elasticsearch.search(
            index=current_app.config['SEARCH_INDEX_NAME'],
            body={
                'query': {
                    'term': {
                        'ident': {
                            'value': code,
                            'case_insensitive': True
                        }
                    }
                }
            }
        )
    except TransportError:
        return None
    if q['timed_out'] is False and q['hits']['total']['value'] > 0:
        return q['hits']['hits'][0]['_source']['name']
    else:
        return None
