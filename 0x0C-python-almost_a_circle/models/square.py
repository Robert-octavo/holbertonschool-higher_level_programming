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

    def update(self, *args, **kwargs):
            """public method that assigns an argument to each attribute"""
            if args and len(args) != 0:
                j = 0
                for i in args:
                    if j == 0:
                        self.id = i
                    elif j == 1:
                        self.size = i
                    elif j == 2:
                        self.x = i
                    elif j == 3:
                        self.y = i
                    j = j + 1
            elif kwargs and len(kwargs) != 0:
                """ that assigns a key/value argument to attributes:"""
                for key, value in kwargs.items():
                    if key == "id":
                        self.id = value
                    elif key == "size":
                        self.size = value
                    elif key == "x":
                        self.x = value
                    elif key == "y":
                        self.y = value

    def to_dictionary(self):
        """that returns the dictionary representation of a Rectangle"""
        """Retur a Key/value"""
        dictionary = {"id": self.id, 
                    "height": self.height,
                    "x": self.x,
                    "y": self.y 
                    }
        return dictionary