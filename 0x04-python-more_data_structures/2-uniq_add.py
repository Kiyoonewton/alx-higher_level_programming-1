#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    uniqinteger = set(my_list)
    for num in uniqinteger:
        sum += num
    return (sum)
