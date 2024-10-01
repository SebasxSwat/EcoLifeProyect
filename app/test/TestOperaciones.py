import pytest


def suma (a, b):
    return a + b

def resta (a, b):
    return a - b

def multiplicacion (a, b):
    return a * b

def division (a, b):
    return a / b

def test_suma():
    assert suma (4, 5) == 9
    assert suma (-3, 5) == 2
    assert suma (0, 0) == 0
    assert suma (2.3, 1.2)== 3.5

def test_resta():
    assert resta (4, 2) == 2
    assert resta (-4, -1) == -3
    assert resta (4.5, 2.1) == 2.4
    assert resta (0, 0) == 0
