#!/usr/bin/python3
# Bello Abayomi

def element_at(my_list, idx):
    """These code retrieve an element from a list like in C."""
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    return (my_list[idx])
