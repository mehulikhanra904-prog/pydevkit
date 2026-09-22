from pydevkit.calculator import (
    add,
    subtract,
    multiply,
    divide,
    calculate,
)


def test_add():
    assert add(10, 20) == 30


def test_subtract():
    assert subtract(20, 10) == 10


def test_multiply():
    assert multiply(5, 4) == 20


def test_divide():
    assert divide(20, 5) == 4


def test_calculate():
    assert calculate("20+70") == 90
    assert calculate("50-20") == 30
    assert calculate("10*5") == 50
    assert calculate("100/4") == 25