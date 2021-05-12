from avw.models import User

def test_new_user(new_user: User):
    assert new_user.username == 'Joe'
    assert new_user.email == 'example@example.com'
    assert new_user.password_hash != 'VerySecure'
    assert new_user.validate_password('VerySecure') is True

def test_get_favorite_airports(new_user: User):
    apts = new_user.get_favorite_airports()
    assert apts is not None
    assert type(apts) == list

def test_add_favorite_airport(new_user: User):
    new_user.add_airport_to_favorites('EPKK')
    apts = new_user.get_favorite_airports()
    assert 'EPKK' in apts

def test_remove_favorite_airport(new_user: User):
    new_user.add_airport_to_favorites('EPKK')
    apts = new_user.get_favorite_airports()
    assert 'EPKK' in apts
    new_user.remove_airport_from_favorites('EPKK')
    apts = new_user.get_favorite_airports()
    assert 'EPKK' not in apts

def test_get_preferences(new_user: User):
    pref = new_user.get_preferences()
    assert pref is not None
    assert type(pref) == dict

def test_update_preferences(new_user: User):
    new_user.update_preferences({'alt_units': 'meters'})
    pref = new_user.get_preferences()
    assert 'alt_units' in pref
    assert pref['alt_units'] == 'meters'
    
def test_hash_password():
    hash = User.hash_password('NewPass')
    assert hash is not None
    assert hash != 'NewPass'

def test_change_password(new_user: User):
    old_hash = new_user.password_hash
    new_user.set_password('NewPass')
    assert old_hash != new_user.password_hash

def test_validate_password(new_user: User):
    new_user.set_password('NewPass')
    assert new_user.validate_password('NewPass') == True

def test_change_email(new_user: User):
    old_email = new_user.email
    new_user.set_email('1' + old_email)
    assert new_user.email != old_email

def test_change_nickname(new_user: User):
    old_nickname = new_user.email
    new_user.set_email('1' + old_nickname)
    assert new_user.email != old_nickname
