#!/usr/bin/python3
""" Function that reads a text file """

def read_file(filename=""):
    """ Function that reads a text file
       """
    with open(filename, 'r', encoding="utf-8") as f:
        read_file = f.read()
        print(read_file, end='')
