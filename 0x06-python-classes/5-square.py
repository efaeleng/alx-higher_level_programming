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

    @property
    def size(self):
        """ Get the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ set the size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """ Method that prints a square with # character
        """
        if not self.__size:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()

