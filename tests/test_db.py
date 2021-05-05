from avw.models import User
from avw import db

def test_db_insert_delete(client, new_user: User):
    db.session.add(new_user)
    db.session.commit()

    # u = db.session.query(User.username == new_user.username).first()
    u = User.query.filter_by(username=new_user.username).first()
    assert u == new_user

    db.session.delete(u)
    db.session.commit()
    u = User.query.filter_by(username=new_user.username).first()
    assert u == None

def test_db_favorite_airports_insert_delete(client, new_user: User):
    l = ['EPKK', 'EPWA']
    new_user.favorite_airports = l
    db.session.add(new_user)
    db.session.commit()

    u = User.query.filter_by(username=new_user.username).first()
    assert u.favorite_airports == l

    db.session.delete(u)
    db.session.commit()
    u = User.query.filter_by(username=new_user.username).first()
    assert u == None


def test_db_preferences_insert_delete(client, new_user: User):
    d = {'pref1': True, 'pref2': 'm', 'pref3': 123}
    new_user.preferences = d
    db.session.add(new_user)
    db.session.commit()

    u = User.query.filter_by(username=new_user.username).first()
    assert u.preferences == d

    db.session.delete(u)
    db.session.commit()
    u = User.query.filter_by(username=new_user.username).first()
    assert u == None