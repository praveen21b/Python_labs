# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 22:26:18 2021

@author: Praveen
"""

print('ABDB'.lower())


# Cycle usage   

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
    

import string

def encrypt_message(text):
    alph = string.ascii_lowercase[:4]
    print(alph)
    new = ''
    for value in text.lower():
        idx = alph.index(value)
        #print(idx)
        encr = (idx+1) % 4
        #print(encr)
        new += (alph[encr])
    return new

print(encrypt_message('BCAB'))