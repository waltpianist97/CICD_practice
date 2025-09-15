import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mymodule import add, divide, subtract,sqrt

def test_add():
    assert add(1, 1) == 2

def test_divide():
    assert divide(4, 2) == 2

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(4, 0)

def test_subtract():
    assert subtract(4, 2) == 2

def test_sqrt():
    assert sqrt(16) == 4

def test_sqrt_negative():
    with pytest.raises(ValueError):
        sqrt(-1)