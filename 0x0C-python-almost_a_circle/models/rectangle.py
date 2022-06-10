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
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    @property
    def width(self):
        """the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
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
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Rectangle's area"""
        return self.width * self.height

    def display(self):
        """that prints in stdout the Rectangle instance with the character #"""
        for i in range(self.height):
            for j in range(self.width):
                print("#", end="")
            print()

