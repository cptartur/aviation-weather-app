from avw import db
from avw.models import User, load_user


def test_load_user(client, new_user: User):
    db.session.add(new_user)
    db.session.commit()

    assert load_user(1) == new_user
    assert load_user('1') == new_user
    assert load_user(2) is None
    assert load_user('2') is None
    assert load_user('fdsafskaj') is None
    assert load_user('') is None
    assert load_user('2\3sd') is None
