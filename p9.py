# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 00:59:38 2021

@author: Praveen
"""

# Define an only_evens function that accepts a list of numbers. 
# It should return a new list consisting of only the even numbers from the original list.
#
# EXAMPLES
# only_evens([4, 8, 15, 16, 23, 42]) => [4, 8, 16, 42]
# only_evens([1, 3, 5])              => []
# only_evens([])                     => []

def only_evens(lists):
    even = []
    for num in lists:
        if num%2 == 0:
            even.append(num)
    return even
print(only_evens([4, 8, 15, 16, 23, 42]))

# Define a long_strings function that accepts a list of strings. 
# It should return a new list consisting of only the strings that have 5 characters or more.
#
# EXAMPLES
# long_strings(["Hello", "Goodbye", "Sam"])  => ["Hello", "Goodbye"]
# long_strings(["Ace", "Cat", "Job"])        => []
# long_strings([])                           => []

def long_strings(lists):
    new = []
    for value in lists:
        if len(value) >= 5:
            new.append(value)
    return new
print(long_strings(["Hello", "Goodbye", "Sam"]))


# Write a factors function that accepts a positive whole number
# It should return a list of all of the number's factors in ascending order
# HINT: Could the range function be helpful here? Or maybe a while loop?
#
# EXAMPLES
# factors(1)  => [1]
# factors(2)  => [1, 2]
# factors(10) => [1, 2, 5, 10]
# factors(64) => [1, 2, 4, 8, 16, 32, 64]

def factors(number):
    return [num for num in range(1,number+1) if number%num==0]
print(factors(64))