#!/usr/bin/python3
"""Define a class square"""


class Square:
    """Represent a Square"""

    def __init__(self, size=0):
        """Initialize a square.

        Args:
            size(int): the size of a new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2
