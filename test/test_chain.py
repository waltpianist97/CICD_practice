# test_chain.py
import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mymodule import add, divide

@pytest.mark.dependency()
def test_step1():
    assert add(1, 1) == 2

@pytest.mark.dependency(depends=["test_step1"])
def test_step2():
    result = add(2, 3)
    assert result == 5

@pytest.mark.dependency(depends=["test_step2"])
def test_step3():
    result = divide(10, 2)
    assert result == 5

@pytest.mark.dependency(depends=["test_step3"])
def test_step4():
    # divisione per zero gestita
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
        
@pytest.mark.dependency(depends=["test_step4"])
def test_step5():
    # piccolo “scherzetto” finale
    assert add(3, 3) == 6
