#!/usr/bin/python3
"""Define a square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """initialize a square.
        
        Args:
            size (int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """defines the area of the new square"""
        return(self.__size ** 2)
