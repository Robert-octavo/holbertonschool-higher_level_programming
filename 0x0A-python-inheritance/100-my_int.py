#!/usr/bin/python3
"""
Write a class MyInt that inherits from int:

    - MyInt is a rebel. MyInt has == and != operators inverted
    - You are not allowed to import any module

Documentation:
https://docs.python.org/3/reference/datamodel.html#object.__eq__
    - object.__lt__(self, other)
    - object.__le__(self, other)
    - object.__eq__(self, other)
    - object.__ne__(self, other)
    - object.__gt__(self, other)
    - object.__ge__(self, other)

    These are the so-called “rich comparison” methods. The correspondence
    between operator symbols and method names is as follows:
        * x<y calls x.__lt__(y),
        * x<=y calls x.__le__(y),
        * x==y calls x.__eq__(y),
        * x!=y calls x.__ne__(y),
        * x>y calls x.__gt__(y),
        * and x>=y calls x.__ge__(y)

    super()
    https://docs.python.org/3/library/functions.html?highlight=super#super
    Return a proxy object that delegates method calls to a parent or sibling
    class of type. This is useful for accessing inherited methods that have
    been overridden in a class.

"""


class MyInt(int):
    """class my int"""
    def __eq__(self, other):
        """Equality == Not Equal."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Not Equal == Equal."""
        return super().__eq__(other)
