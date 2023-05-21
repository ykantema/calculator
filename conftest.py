import math

from calculator import Calculator, fn_plus, fn_multiplied
import pytest


@pytest.fixture(scope="session")
def calculator():
    return Calculator()


@pytest.fixture(scope="module")
def calculator_plus(calculator):
    calculator.set_function(fn_plus)
    return calculator


@pytest.fixture(scope="module")
def calculator_multiplied(calculator):
    calculator.set_function(fn_multiplied)
    return calculator


def fn_is_equal(self, a, b):
    assert self.__class__.__name__ == 'Calculator'
    dict_a = {}
    dict_b = {}
    while a > 0:
        for _dict, number in [(dict_b, b), (dict_a, a)]:
            last_number = number % 10
            if last_number in _dict.keys():
                _dict[last_number] += 1
            else:
                _dict[last_number] = 1
        a //= 10
        b //= 10
    for k in dict_a.keys():
        if not k in dict_b.keys() or not dict_a[k] == dict_b[k]:
            return False
    return True


@pytest.fixture(scope="module")
def calculator_equal(calculator):
    calculator.set_function(fn_is_equal)
    return calculator
