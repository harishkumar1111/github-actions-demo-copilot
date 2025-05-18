import pytest
from calc import *

# @pytest.fixture
# def calc():
#     return Calculator()

def test_add(calc):
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0

def test_subtract(calc):
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(0, 5) == -5
    assert calc.subtract(-2, -2) == 0

def test_multiply(calc):
    assert calc.multiply(4, 3) == 12
    assert calc.multiply(-2, 3) == -6
    assert calc.multiply(0, 100) == 0

def test_div(calc):
    assert calc.div(10, 2) == 5
    assert calc.div(-6, 3) == -2
    assert calc.div(0, 1) == 0

def test_divide_by_zero(calc):
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        calc.div(5, 0)