from flask import current_app
from collections import OrderedDict
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
                                    'fields': ['ident', 'name']
                                }
                            }
                        ],
                        'filter': [
                            {
                                'term': {'type': 'large_airport'}
                            }
                        ]
                    }
                }
            }
        )
    except TransportError as e:
        return None
    
    print(q)
    if q['timed_out'] is False and q['hits']['total']['value'] > 0:
        return sorted(q['hits']['hits'], key=lambda k: k['_score'], reverse=True)
    else:
        return None
