import string

import pytest

from src.fizzbuzz import Fizzbuzz


def test_fizzbuzz():
    fizzbuzz = Fizzbuzz()

def test_call():
    fizzbuzz = Fizzbuzz()
    fizzbuzz.call(1)

def test_input():
    fizzbuzz = Fizzbuzz()
    fizzbuzz.is_int(1)

def test_input_is_integer():
    fizzbuzz = Fizzbuzz()
    is_integer = fizzbuzz.is_int("abc")
    assert not is_integer

def test_input_is_not_integer():
    fizzbuzz = Fizzbuzz()
    with pytest.raises(ValueError):
        fizzbuzz.call("abc")

def test_output():
    fizzbuzz = Fizzbuzz()
    output = fizzbuzz.call(1)
    assert isinstance(output, str)

def test_multiple_of_three():
    fizzbuzz = Fizzbuzz()
    for number in range(100):
        if number % 3 == 0:
            output = fizzbuzz.call(number)
            assert  output == "fizz"


