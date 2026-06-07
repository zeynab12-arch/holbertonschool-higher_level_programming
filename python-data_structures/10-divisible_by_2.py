#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    m = []
    for i in my_list:
        if i % 2 == 0:
            m.append(True)
        else:
            m.append(False)
    return m