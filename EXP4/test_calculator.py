# test_calculator.py
import EXP4.calculator as calc

def test_addition():
    assert calc.calculate(2, "+", 3) == 5

def test_subtraction():
    assert calc.calculate(5, "-", 2) == 3

def test_multiplication():
    assert calc.calculate(3, "*", 4) == 12

def test_division():
    assert calc.calculate(10, "/", 2) == 5

def test_division_by_zero():
    assert calc.calculate(5, "/", 0) == "Error! Division by zero."

def test_invalid_operator():
    assert calc.calculate(5, "%", 2) == "Invalid operator."
