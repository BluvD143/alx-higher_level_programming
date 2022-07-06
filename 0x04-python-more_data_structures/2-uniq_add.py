#!/usr/bin/python3
# 2-uniq_add.py

def uniq_add(my_list=[]):
    #   set is used because it doesn't allow duplicate values
    res = 0
    for num in set(my_list):
        res += num
    return res
