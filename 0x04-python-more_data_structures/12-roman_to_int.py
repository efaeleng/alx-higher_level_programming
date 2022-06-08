#!/usr/bin/python3
def roman_to_int(roman_string):
    val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    x = 0

    if type(roman_string) is str and roman_string:
        for i in range(len(roman_string) - 1, -1, -1):
            if val[roman_string[i]] >= p:
                num += val[roman_string[i]]
            else:
                num -= val[roman_string[i]]
                x = val[roman_string[i]]
    return
