from avw.airport import bp


@bp.app_template_filter()
def decode_clouds(code):
    d = {
        'FEW': 'Few',
        'SCT': 'Scattered',
        'BKN': 'Broken',
        'OVC': 'Overcast',
        'CLR': 'Clear',
        'CAVOK': 'Clear'
    }
    print(code)
    return d.get(code, code)
