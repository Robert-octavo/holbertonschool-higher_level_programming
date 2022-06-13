#!/usr/bin/python3
"""Class Rectangle"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """class square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """use to print and str of the rectangle"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"

    @property
    def size(self):
        """the width of the Rectangle."""
        return self.height

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
