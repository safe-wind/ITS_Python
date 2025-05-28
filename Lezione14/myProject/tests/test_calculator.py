from myProject.calculator import Calculator
import pytest

'''
def test_addiction():
    calculation:Calculator = Calculator(10,5)
    assert calculation.addiction() == 13, "The sum is wrong"

def test_subtraction():
    calculation:Calculator = Calculator(10,5)
    assert calculation.subtraction() == 5, "The subraction is wrong"

def test_multiplication():
    calculation:Calculator = Calculator(10,5)
    assert calculation.multiplication() == 50, "The multiplication is wrong"

def test_division():
    calculation:Calculator = Calculator(10,5)
    assert calculation.division() == 2.00, "The quotient is wrong"'''

@pytest.fixture
def calculation():
    return Calculator(10,5)

def test_addiction(calculation):
    assert calculation.addiction() == 13, "The sum is wrong"

def test_subtraction(calculation):
    assert calculation.subtraction() == 5, "The subtraction is wrong"

def test_multiplication(calculation):
    assert calculation.multiplication() == 50, "The multiplication is wrong"

def test_division(calculation):
    assert calculation.division() == 2.00, "The quotient is wrong"