from numb3rs import validate


def test_validate():
    assert validate("255.255.255.255") == True
    assert validate("192.168.1.1") == True
    assert validate("192.168.1.255") == True
    assert validate("0.0.0.0") == True
    assert validate("192.168.1") == False
    assert validate("192.168.1.256") == False
    assert validate("192.168.1.255.1") == False
    assert validate("512.512.512.512") == False
    assert validate("512.512.512.512.512") == False
    assert validate("cat") == False
    assert validate("") == False
    assert validate("-1.0.0.0") == False
    assert validate("192.-1.1.1") == False
    assert validate("192.1.5.3a") == False
    assert validate("1.2.3.4 ") == False
    assert validate(" 1.2.3.4") == False
    assert validate("1..2.3") == False
    assert validate("1.2.3.") == False
