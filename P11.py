# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 19:03:09 2021

@author: Praveen
"""

# Define an encrypt_message function that accepts a string.
# The input string will consist of only alphabetic characters.
# The function should return a string where all characters have been moved
# "up" two spots in the alphabet. For example, "a" will become "c".
#
# EXAMPLES
# encrypt_message("abc") => "cde"
# encrypt_message("xyz") => "zab"
# encrypt_message("")    => ""

import string

def encrypt_message(text):
    alph = string.ascii_lowercase
    print(alph)
    new = ''
    for value in text.lower():
        idx = alph.index(value)
        #print(idx)
        encr = (idx+2) % 26
        #print(encr)
        new += (alph[encr])
    return new

print(encrypt_message('SHASHANK'))


print('ABDB'.lower())


    

from itertools import cycle
letter = cycle('ABCD'.lower())
print(letter)
n1 = ''
for value in letter:
    #print(value)
    n1 += value
    if len(n1) > 20:
        break
print(n1)
    
    