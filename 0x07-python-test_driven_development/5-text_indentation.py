#!/usr/bin/python3
"""
    Function to change the
    indentation of a text
"""


def text_indentation(text):
    """text_indentation"""
    flag = 0
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for i in range(len(text)):
        if flag == 0:
            if (text[i] != '.' and text[i] != '?' and text[i] != ':'):
                print("{:s}".format(text[i]), end="")
            else:
                print("{:s}\n".format(text[i]))
                flag = 1
        else:
            for j in range(i, len(text)):
                if text[j] != ' ':
                    flag = 0
                    i = j
                    break
