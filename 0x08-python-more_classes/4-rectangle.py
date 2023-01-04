#!/usr/bin/python3
"""Represent a class"""


class Rectangle:
    """Defines a rectangle by its width and height"""

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle with the given width and height """

        self.width = width
        self.height = height

    @property
    def width(self):
        """int: The width of the rectangle"""

        return self._width

    @width.setter
    def width(self, value):
        """set the width of the rectangle"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """int: The height of the rectangle."""

        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Returns the area of the rectangle."""

        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""

        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a string representation of the rectangle"""

        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join("#" * self.width for _ in range(self.height))

    def __repr__(self):
        """Returns a string representation of the rectangle"""

        return f"Rectangle({self.width}, {self.height})"
