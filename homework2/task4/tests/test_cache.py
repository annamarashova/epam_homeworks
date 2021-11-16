import pytest
from task4.cache import cache


@cache
def difficult_function(x):
    return x ** 10


@cache
def difficult_function_2(x):
    factorial = 1
    for i in range(2, x + 1):
        factorial *= i
    return factorial


def test_difficult_function():
    a = difficult_function(15)
    b = difficult_function(15)
    assert a is b


def test_difficult_function_2():
    a = difficult_function(2)
    b = difficult_function_2(2)
    assert a is not b
