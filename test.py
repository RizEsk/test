import pytest



def first(x):
    return x + 1

def test1():
    assert first(3) == 4
    
def test2():
    assert first(5) == 6

def test3():
    r= 5+1    
    assert first(6) == r