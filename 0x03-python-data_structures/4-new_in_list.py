#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_copy = my_list.copy()
    if idx >= 0 and idx < len(my_list):
        new_copy[idx] = element
    return new_copy
            
