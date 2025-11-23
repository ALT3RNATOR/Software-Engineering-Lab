"""
shapes_sphinx.py

Example module for Ex6 showing functions, classes,
and reStructuredText-style docstrings for Sphinx.
"""

from dataclasses import dataclass
from typing import Iterable


def add(a: float, b: float) -> float:
    """Add two numbers.

    :param a: First number.
    :type a: float
    :param b: Second number.
    :type b: float
    :return: Sum of ``a`` and ``b``.
    :rtype: float

    Example::

        >>> add(2, 3)
        5
    """
    return a + b


def average(values: Iterable[float]) -> float:
    """Compute the arithmetic mean of a sequence of numbers.

    :param values: Iterable of numeric values.
    :type values: Iterable[float]
    :raises ValueError: If ``values`` is empty.
    :return: Arithmetic mean of the values.
    :rtype: float
    """
    values = list(values)
    if not values:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)


@dataclass
class Rectangle:
    """Represent a rectangle.

    :param width: Rectangle width.
    :type width: float
    :param height: Rectangle height.
    :type height: float
    """

    width: float
    height: float

    def area(self) -> float:
        """Return the area of the rectangle.

        :return: Area = ``width * height``.
        :rtype: float
        """
        return self.width * self.height

    def perimeter(self) -> float:
        """Return the perimeter of the rectangle.

        :return: Perimeter = ``2 * (width + height)``.
        :rtype: float
        """
        return 2 * (self.width + self.height)
