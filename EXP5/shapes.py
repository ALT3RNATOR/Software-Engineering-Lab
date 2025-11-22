"""
shapes.py

Example module demonstrating functions, classes, and docstrings
for Software Engineering Lab EXP5.
"""

from dataclasses import dataclass
from typing import Iterable


def add(a: float, b: float) -> float:
    """Add two numbers.

    Args:
        a: First number.
        b: Second number.

    Returns:
        The sum of ``a`` and ``b``.

    Examples:
        >>> add(2, 3)
        5
    """
    return a + b


def average(values: Iterable[float]) -> float:
    """Compute the average of a sequence of numbers.

    Args:
        values: Any iterable of numeric values.

    Returns:
        The arithmetic mean of all values.

    Raises:
        ValueError: If ``values`` is empty.

    Examples:
        >>> average([1, 2, 3, 4])
        2.5
    """
    values = list(values)
    if not values:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)


@dataclass
class Rectangle:
    """Represent a rectangle shape.

    Attributes:
        width: The width of the rectangle (must be non-negative).
        height: The height of the rectangle (must be non-negative).
    """

    width: float
    height: float

    def area(self) -> float:
        """Calculate the area of the rectangle.

        Returns:
            The area as ``width * height``.

        Examples:
            >>> rect = Rectangle(3, 4)
            >>> rect.area()
            12
        """
        return self.width * self.height

    def perimeter(self) -> float:
        """Calculate the perimeter of the rectangle.

        Returns:
            The perimeter as ``2 * (width + height)``.

        Examples:
            >>> rect = Rectangle(3, 4)
            >>> rect.perimeter()
            14
        """
        return 2 * (self.width + self.height)
