# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 14:06:07 2021

@author: Praveen
"""
import copy

a = [1,3,[7,8,9],4,6]
b = a[:]
c = a.copy()
# shallow copy
d = copy.copy(a)
e = copy.deepcopy(a)

print(a)
print(b)
print(c)
print(d)
print(e)

print()
a[2].append(80)
print(a)
print(b)
print(c)
print(d)
print(e)


words = ['danger', 'beware', 'danger']
count = {}
def re_count(words):
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count
print(re_count(words))

