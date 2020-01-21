#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, mode="r", encoding="UTF-8") as f:
        flines = f.readlines()
        if nb_lines <= 0 or nb_lines >= len(flines):
            for line in flines:
                print(line, end="")
        else:
            for i in range(nb_lines):
                print(flines[i], end="")
