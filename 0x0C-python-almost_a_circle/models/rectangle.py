#!/usr/bin/python3
"""Class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """class rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """use to print and str of the rectangle"""
        _i = self.id
        _x = self.x
        _y = self.y
        _w = self.width
        _h = self.height
        return f"[Rectangle] ({_i}) {_x}/{_y} - {_w}/{_h}"

    @property
    def width(self):
        """the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Method setter to set width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 1:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Method setter to set height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 1:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Method setter to set x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Method setter to set y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Rectangle's area"""
        return self.width * self.height

    def display(self):
        """that prints in stdout the Rectangle instance with the character #"""
        [print("")for y in range(self.y)]
        for i in range(self.height):
            [print(" ", end="")for x in range(self.x)]
            for j in range(self.width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """public method that assigns an argument to each attribute"""
        if args and len(args) != 0:
            j = 0
            for i in args:
                if j == 0:
                    self.id = i
                elif j == 1:
                    self.width = i
                elif j == 2:
                    self.height = i
                elif j == 3:
                    self.x = i
                elif j == 4:
                    self.y = i
                j = j + 1
        elif kwargs and len(kwargs) != 0:
            """ that assigns a key/value argument to attributes:"""
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """that returns the dictionary representation of a Rectangle"""
        """Retur a Key/value"""
        dictionary = {
                        "id": self.id,
                        "width": self.width,
                        "height": self.height,
                        "x": self.x,
                        "y": self.y}
        return dictionary
