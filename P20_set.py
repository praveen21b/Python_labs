# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 22:46:36 2021

@author: Praveen
"""

# Define a remove_duplicates function that accepts a single list as an argument. 
# The function should return a list with all of the duplicates from the original list removed. 
# The order of elements in the returned list is irrelevant.
#
# EXAMPLES:
# remove_duplicates([1, 2, 1, 2])  => [1, 2] or [2, 1]
# remove_duplicates([1, 2, 3, 4])  => [1, 2, 3, 4] in some order

def remove_duplicates(lists):
    return list(set(lists))
print(remove_duplicates([1, 2, 1, 2]))
print(remove_duplicates([1, 2, 3, 4]) )
    