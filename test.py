from main import calculator

def test1():
    res = calculator(2,2,'+')
    assert res == 4

def test2():
    res = calculator(3,1,'-')
    assert res == 2