# EXP5 – Docstrings and MkDocs

This experiment demonstrates:

- Writing Python functions and classes
- Documenting them using **docstrings**
- Generating HTML documentation using **MkDocs**

---

## Module: shapes.py

This module contains well-documented functions and a class.

### Function: add(a, b)
Adds two numbers and returns the result.

### Function: average(values)
Calculates the average of a list of numbers. Raises ValueError if the list is empty.

### Class: Rectangle
Represents a rectangle with:
- area()
- perimeter()

Example:

```python
from shapes import Rectangle

rect = Rectangle(3, 4)
print(rect.area())      # 12
print(rect.perimeter()) # 14
