# test_shapes.py

from EXP5.shapes import add, average, Rectangle
import pytest


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_average():
    assert average([1, 2, 3, 4]) == 2.5
    with pytest.raises(ValueError):
        average([])


def test_rectangle():
    rect = Rectangle(3, 4)
    assert rect.area() == 12
    assert rect.perimeter() == 14
