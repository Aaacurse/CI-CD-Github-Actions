from src.python_file import add,subtract

def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0
    assert(-1,-1)==-2

def test_subtract():
    assert subtract(5,3)==2
    assert(2,2)==0
    assert(1,-1)==2
    assert(3,5)==-2