import pytest
from seasons import season

def test_invalid_date():
    """"""
    testuser = season("1999-01-01")
    assert str(testuser) == "Twelve million, eight hundred fifty-six thousand, three hundred twenty minutes"