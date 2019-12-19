#!/usr/bin/python3
def uniq_add(my_list=[]):
    list = {i for i in my_list}
    return sum(list)
