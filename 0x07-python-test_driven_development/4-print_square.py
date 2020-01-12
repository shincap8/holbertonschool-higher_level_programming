#!/usr/bin/python3
"""Function to print a square"""


def print_square(size):
    """print_square"""
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise TypeError('size must be >= 0')
    for i in range(size):
        for j in range(size):
            print('#', end="")
        print()
