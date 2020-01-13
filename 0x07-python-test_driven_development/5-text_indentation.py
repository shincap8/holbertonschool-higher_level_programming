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
        if i == 0 and text[i] == ' ':
            flag = 1
        if flag == 0:
            if (text[i] != '.' and text[i] != '?' and text[i] != ':'):
                    print("{:s}".format(text[i]), end="")
            else:
                print("{:s}\n".format(text[i]))
                flag = 1
        else:
            if text[i] != ' ':
                flag = 0
                if (text[i] != '.' and text[i] != '?' and text[i] != ':'):
                    print("{:s}".format(text[i]), end="")
                else:
                    print("{:s}\n".format(text[i]))
                    flag = 1
