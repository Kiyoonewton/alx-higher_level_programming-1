#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """find all multiples of 2 in a list"""
    aggregate = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            aggregate.append(True)
        else:
            aggregate.append(False)

    return(aggregate)
