import pytest
from math_utils import add, divide, is_even

def test_add_numbers():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_divide_numbers():
    assert divide(10, 2) == 5
    assert divide(-9, 3) == -3

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)

@pytest.mark.parametrize("num,expected", [
    (2, True),
    (3, False),
    (0, True),
    (-4, True),
])
def test_is_even(num, expected):
    assert is_even(num) == expected
