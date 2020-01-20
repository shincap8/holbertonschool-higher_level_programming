#!/usr/bin/python3
"""Object My list"""


class MyList(list):
    """
        method to print sorted
    """
    def print_sorted(self):
        print(sorted(self))
