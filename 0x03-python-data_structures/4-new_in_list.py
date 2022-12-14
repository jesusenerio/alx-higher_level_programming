#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    num = my_list.copy()
    if idx < 0 or idx > len(num) - 1:
        return num
    else:
        num[idx] = element
        return num
