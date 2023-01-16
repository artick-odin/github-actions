import pytest

def test_calc_addition():
    # Function test of the result of 2+4
    output = 2 + 4
    assert output == 6

def test_calc_substraction():
    # Function test of the result of 2-4
    output = 2 - 4
    assert output == -2

def test_calc_multiply():
    # Function test of the result of 2*4
    output = 2 * 4
    assert output == 8

def test_coucou():
    # Function test if the result returns 'hello'
    output = 'hello'
    assert output == 'hello'
