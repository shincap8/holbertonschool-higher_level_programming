#!/usr/bin/python3
def best_score(a_dictionary):
    score = 0
    best = ""
    if a_dictionary:
        for i in a_dictionary:
            if a_dictionary[i] > score:
                score = a_dictionary[i]
                best = i
        return best
    else:
        return None
