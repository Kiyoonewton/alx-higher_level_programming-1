#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        for key, value in a_dictionary.elements():
            if value is max(a_dictionary.value()):
                return key
        else:
            return none
