# test_chain.py
import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mymodule import add


@pytest.mark.dependency()
def test_step1():
    assert add(1, 1) == 2

@pytest.mark.dependency(depends=["test_step1"])
def test_step2():
    assert add(2, 2) == 3

@pytest.mark.dependency(depends=["test_step2"])
def test_step3():
    assert add(3, 3) == 6
