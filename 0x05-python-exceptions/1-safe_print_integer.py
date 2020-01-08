#!/usr/bin/python3
def safe_print_integer(value):
    check = 0
    try:
        check += value
        print("{:d}".format(value))
        return True

    except TypeError:
        return False
