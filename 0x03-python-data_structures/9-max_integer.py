#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list=[]:
        return None

    max = my_list
    for x in my_list:
        if x > max:
            max = x
            return max
