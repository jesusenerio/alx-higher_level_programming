#!/usr/bin/python3
"""Defines an integer addition function"""


def add_integer(a, b=98):
    """Represent an integer addition a and b.

    Floats arguments are typecasted before addition is performed

    Raises:
        TypeError: if either a or b is non-integer or non-float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an interger")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
