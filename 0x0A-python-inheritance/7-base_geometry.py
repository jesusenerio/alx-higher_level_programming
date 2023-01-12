#!/usr/bin/python3
"""Define a class basegeometry"""


class BaseGeometry:
    """Represents a class"""
    def area(self):
        """Not Implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        """Validate a parameter as an integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not
            ValueError: If value is <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
