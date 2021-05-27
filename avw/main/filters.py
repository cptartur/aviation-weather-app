from avw.main import bp
from avw.search import get_airport_name


@bp.app_template_filter('airport_name')
def airport_name(code):
    return get_airport_name(code) or code
