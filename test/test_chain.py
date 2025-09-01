# test_chain.py
import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mymodule import add

state = {"last_result": None}

def test_step1():
    state["last_result"] = add(1, 1)
    assert state["last_result"] == 2

def test_step2():
    # Dipende dal risultato del test_step1
    assert state["last_result"] == 2
    state["last_result"] *= 2

def test_step3():
    # Dipende da step2
    assert state["last_result"] == 4
