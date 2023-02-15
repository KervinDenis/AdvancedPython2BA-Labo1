import pytest
import utils

def test_fact():
    assert(fact(5), 120)
    
def test_roots():
    assert(roots(1, 0, 1), (-1j, 1j))

def test_integrate():
    assert(integrate('x ** 2 - 1', -1, 1),-1.3333333333333335)
