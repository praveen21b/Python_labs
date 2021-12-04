# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 09:54:01 2021

@author: Praveen
"""

# Recusrsion

def count_down(number):
    while number > 0:
        print(number)
        number -= 1
        
count_down(5)

def count_down_rec(number):
    if number <= 0:
        return
    print(number)
    count_down_rec(number-1)
    
count_down_rec(5)


def reverse(string):
    return string[::-1]
print(reverse('STRAW'))

def reverse_while(string):
    new = ''
    i = len(string)-1
    while  i > 0:
        new = new + string[i]
        i -=1
    return new
print(reverse('STRAW'))

def reverse_rec(string):
    if len(string) <=0:
        return string
    return string[-1]+ reverse_rec(string[:-1])
print(reverse('STRAW'))


# Define a function called "factorial" that accepts a single number as input
#
# A factorial represents the product of all numbers up to, and including, that number. 
# For example, 5 factorial is 5 * 4 * 3 * 2 * 1 = 120
#
# Return the factorial calculation from your function. You should NOT use any kind of loops. 
# Instead, utilize recursion. Your function MUST call itself.
# See sample inputs and return values below
#
# factorial(1) => 1
# factorial(2) => 2
# factorial(3) => 6
# factorial(4) => 24
# factorial(5) => 120

def factorial(number):
    if number == 1:
        return number
    return number * factorial(number-1)
print(factorial(1))
print(factorial(5))

print(range(0,4))