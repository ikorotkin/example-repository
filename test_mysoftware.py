from mysoftware import *

def test_square_integers():
    assert square(2) == 4
    assert square(0) == 0
    assert square(-1) == 1
    assert square(3) == 9

def test_invsqrt():
    assert invsqrt(1) == 1
    assert invsqrt(4) == 0.5
    assert invsqrt(0) == None
    assert invsqrt(-1) == None

