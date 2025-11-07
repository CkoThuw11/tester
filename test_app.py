from utils.app import add, subtract, multiple, divide

def test_add():
    assert add(2, 3) == 5

def test_substract():
    assert subtract(3, 2) == 1

def test_multiple():
    assert multiple(4, 5) == 20

def test_divide():
    assert divide(2, 1) == 2