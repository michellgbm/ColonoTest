from app import restar, sumar


def test_sumar():
    assert sumar(9, 1) == 10

def test_restar():
    assert restar(5, 3) == 2
