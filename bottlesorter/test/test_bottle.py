from bottlesorter.bottle import Bottle

def test_is_bottle_complete():
    b = Bottle(volume=3, name = "bottle1")
    b.contents = ["O", "O", "O"]
    assert b.is_bottle_complete() == True

def test_has_room_true():
    b = Bottle(volume=3, name = "bottle1")
    b.contents = ["O", "O", "O"]
    assert b.has_room() == False

def test_has_room_false():
    b = Bottle(volume=3, name = "bottle1")
    b.contents = ["O", "O"]
    assert b.has_room() == True

def test_valid_pour_true():
    b = Bottle(volume=4, name = "bottle1")
    b.contents = ["O", "O", "O"]
    assert b.valid_pour("O") == True

def test_valid_pour_false():
    b = Bottle(volume=3, name = "bottle1")
    b.contents = ["O", "O", "O"]
    assert b.valid_pour("X") == False