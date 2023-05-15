#!/usr/bin/python3
def no_c(my_string):
    my_new = ""
    for i in my_string:
        if i is not 'c' and i is not 'C':
            my_new += i
    return my_new
