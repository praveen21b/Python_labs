# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 13:48:51 2021

@author: Praveen
"""

# Define an invoke_thrice function.
# It should accept a single argument (which will be a function)
# In its body, the invoke_thrice function should invoke
# the function that's passed in exactly three times.

def invoke_thrice(func):
    func()
    func()
    func()
    
def sample():
    print('A')
    print('a')

invoke_thrice(sample)
print()

def gallons_to_cups(gallons):
    a = gallons_to_quarts(gallons)
    b = quarts_to_pints(a)
    c = pints_to_cups(b)
    return c

def gallons_to_quarts(gallons):
    return 4 * gallons

def quarts_to_pints(gallons):
    return 2 * gallons

def pints_to_cups(gallons):
    return 2 * gallons

print(gallons_to_cups(1))
print(gallons_to_cups(3))
print()

####Nested functions
def gallons_to_cups(gallons):
    def gallons_to_quarts(gallons):
        return 4 * gallons

    def quarts_to_pints(gallons):
        return 2 * gallons

    def pints_to_cups(gallons):
        return 2 * gallons
    
    a = gallons_to_quarts(gallons)
    b = quarts_to_pints(a)
    c = pints_to_cups(b)
    return c

print(gallons_to_cups(1))
print(gallons_to_cups(3),'\n')

# Define an "outer" function that accepts no arguments
# Inside the body of "outer", define an "inner" function
# The "inner" function should return the value 5.
# From "outer", return the uninvoked "inner" function

def outer():
    def inner():
        return 5
    return inner

print(outer()(),'\n')

####
def multiply(a, b):

  return a * b

def divide(a, b):

  return a / b

def calculate(func, a, b):

  return func(a, b)

print(calculate(multiply, 10, 5))

###

import functools
def uppercase(fn):

    @functools.wraps(fn)

    def wrapper(*args, **kwargs):

        #fn(*args, **kwargs).upper()

        return fn(*args, **kwargs).upper()


@uppercase

def concatenate(a, b):

    """Combines two strings together"""

    return a + b



print(concatenate("pyt", "hon"))
