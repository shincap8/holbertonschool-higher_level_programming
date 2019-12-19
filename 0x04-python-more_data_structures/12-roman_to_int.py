#!/usr/bin/python3
def roman_to_int(roman_string):
    value = 0
    result = 0
    roval = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if type(roman_string) is not str or roman_string == "":
        return 0
    else:
        for i in roman_string:
            if result == 0:
                value = roval[i]
            if value < roval[i]:
                result = (result - value) + (roval[i] - value)
                value = roval[i]
            else:
                result = result + roval[i]
                value = roval[i]
        return result
