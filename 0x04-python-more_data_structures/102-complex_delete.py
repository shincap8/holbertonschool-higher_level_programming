#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = list(i for i in a_dictionary)
    for i in keys:
        if value == a_dictionary[i]:
            del a_dictionary[i]
    return a_dictionary
