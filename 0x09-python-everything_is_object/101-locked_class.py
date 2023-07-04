#!/usr/bin/python3
"""

This Defines class with no class or object attribute
Controls dynamically created instance attribute
"""


class LockedClass():
    """
    prevent user from creating a new instance attribute dynamically
    unless attribute it is "first_name"

    >>> m = lockedClass()
    >>> m.first_name = 'Andrew'
    >>> m.first_name
    'Andrew'

    >>> m.last_name = 'Siafa'
    Traceback (most recent call last):

    ...
    AttributeError: 'LockedClass' object has no atribute 'last__name'
    """


    __slots_ = "first_name"
