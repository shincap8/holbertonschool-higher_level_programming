#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        my_list[x - 1]
        for i in range(x):
            print('{:d}'.format(my_list[i]), end="")
        print()
        return x

    except IndexError:
        for i in my_list:
            print('{:d}'.format(i), end="")
            count += 1
        print()
        return count
