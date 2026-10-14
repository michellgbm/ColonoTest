from app import restar, sumar


def test_sumar():
    assert sumar(9, 3) == 12

def test_restar():
    assert restar(5, 3) == 2
