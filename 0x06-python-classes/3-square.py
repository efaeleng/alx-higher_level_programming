#!/usr/bin/python3
""" A class that defines a square by its size
    """


class Square:
    """ A class that defines a square by its size
    """
    def __init__(self, size=0):
        """Initialize a new Square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Method that returns the area of the square
        """
        return (self.__size ** 2)
