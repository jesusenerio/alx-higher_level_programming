#!/usr/bin/python3
#add_integer = __import__('0-add_integer').add_integer
import sys
sys.path.append('../0x07-python-test_driven_development')
from 0x07-python-test_driven_development.0-add_integer import add_integer

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)
