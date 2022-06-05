#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx > len(my_list) or idx < 0:
        return my_list
    return [element if new == my_list[idx] else new for new in my_list]
