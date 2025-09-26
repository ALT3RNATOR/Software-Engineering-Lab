# test_calculator.py
import builtins
import io
from contextlib import redirect_stdout
import importlib

def run_calculator_with_inputs(inputs):
    it = iter(inputs)
    def fake_input(prompt=''):
        return next(it)
    builtins_input = builtins.input
    builtins.input = fake_input
    try:
        f = io.StringIO()
        with redirect_stdout(f):
            if "calculator" in importlib.sys.modules:
                importlib.reload(importlib.import_module("calculator"))
            else:
                importlib.import_module("calculator")
        return f.getvalue()
    finally:
        builtins.input = builtins_input

def test_addition():
    out = run_calculator_with_inputs(["2", "+", "3"])
    assert "Result: 5.0" in out

def test_division_by_zero():
    out = run_calculator_with_inputs(["5", "/", "0"])
    assert "Error! Division by zero." in out

def test_invalid_operator():
    out = run_calculator_with_inputs(["5", "%", "2"])
    assert "Invalid operator." in out
