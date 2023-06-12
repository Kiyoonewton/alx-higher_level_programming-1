#!/usr/bin/python3
"""
    101-add_attribute module
    Function that adds a new attribute to an object if it’s possible
"""


def add_attribute(ukp, allot, value):
    """Function that adds a new attribute to an object if it's possible"""
    if not(hasattr(ukp, '__dict__')):
        raise TypeError("can't add new attribute")
    setattr(cla, allot, value)
