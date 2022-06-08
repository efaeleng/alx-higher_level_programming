#!/usr/bin/python3
def search_replace(my_list, search, replace):
    items = len(my_list)
    new_list = my_list.copy()
    for i in range(items):
        if new_list[i] == search:
            new_list[i] = replace
    return new_list
