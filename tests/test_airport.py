from avw.models import User
from avw import db

def test_add_remove_to_favorites(client):
    user = User('Susan', 'a@a.com', '12345')
    db.session.add(user)
    db.session.commit()

    client.post('/login', data={'username': 'Susan', 'password': '12345'})

    assert user.get_favorite_airports() == []

    client.get('/airport/add/EPKK')
    assert user.get_favorite_airports() == ['EPKK']
    client.get('/airport/add/KLAX')
    assert user.get_favorite_airports() == ['EPKK', 'KLAX']

    client.get('/airport/remove/EPKK')
    assert user.get_favorite_airports() == ['KLAX']
    client.get('/airport/remove/KLAX')
    assert user.get_favorite_airports() == []

    db.session.delete(user)
    db.session.commit()