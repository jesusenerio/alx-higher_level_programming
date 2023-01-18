#!/usr/bin/python3
"""Rectangle subclass"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size):
        """initialize a new square

        Args:
            size(int):the size of the new square
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
