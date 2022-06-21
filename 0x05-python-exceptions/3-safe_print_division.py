#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        var = a / b
    except zero_division_error:
        var = None
    finally:
        print("Inside result: {}".format(var))
    return 
