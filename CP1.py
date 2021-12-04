# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 21:53:01 2021

@author: Praveen
"""

#1 Write a Python program that remove the extra spaces from the following string:
' I am        learning Python      object        oriented     programming '

def removespaces(strings):
    return ' '.join(strings.split())

print(removespaces(' I am        learning Python      object        oriented     programming '))


#2 Write a python program that reverse the case of string :
string = "I am a python developer"

def rev(strings):
    return strings.swapcase()

print(rev(string),'\n')


#3 Display the number of letters in the string:
my_word = "Python is wonderful"

def num_of_str(word):
    # No of char in string
    # return len(word)
    return len(''.join(word.split()))

print(num_of_str(my_word),'\n')

#4 Concatenate the following two strings together:
string_left = "Spider"
string_right = "man"

def join_strings(str1,str2):
    return str1 + str2
print(join_strings(string_left, string_right),'\n')

#5 to lowercase
string1 = "Python"
string2 = "Programming"
string3 = "Language"

print(string1.lower(),'\n')

#6 Replace every occurrence of the character "s" with the character "x"
phrase = "Somebody said something to Sara."
print(phrase.replace('s','x'))

#7 In one of  Famous Coffee Mixer shops chain every 6 days with every day one 
# cup of coffee customer buys, customer gets a 7th cup free in the weekend (Sunday)!
# Create a Python program that takes numbers of cups bought and return the total 
# number of cups that customer would get and
# also the number of  free cups for one month( for both 30 days & 31 days)

n = 30
def total_cups_cust(n):
    return n//6 + n
total_cups = total_cups_cust(n)
def total_cups_gets_free(total_cups):
    return round(total_cups/6, 0)
print(('Total cups for 30 days = ') + str(total_cups_cust(n)))
print(('Free cups in 30 days = ') + str(total_cups_gets_free(total_cups)))
     
n = 31
print(('Total cups for 31 days = ') + str(total_cups_cust(n)))
print(('Free cups in 31 days = ') + str(total_cups_gets_free(total_cups)))

print()

import copy as c
a = [1,2,[4,5,8],7]
b = c.deepcopy(a)
d = c.copy(a)
print(b)
print(d)
print()
print(a)
b.append(1)
d.append(1)
print(a)
print(b)
print(d)


name = 'Shashank@Kumar'
name = name.split('@')[::-1]
print('_'.join(name) +"8")

mName = 'Shashank'
name = 'Shashamk'
for idx,value in enumerate(mName):
    if value not in name:
        print(name[idx])
        name = name.replace(name[idx],mName[idx])
        print(name)