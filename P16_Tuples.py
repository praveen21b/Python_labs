# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 11:01:11 2021

@author: Praveen
"""

empty = 1,
print(empty)
print(type(empty))

numbers_a = 1,2,3
numbers_b = 4,5,6
numbers_c = 7,8,9
all_numbers = tuple([numbers_a, numbers_b, numbers_c])
print(all_numbers)


# Declare a sum_of_evens_and_odds function that accepts a tuple of numbers.
# It should return a tuple with two numeric values:
# -- the sum of the even numbers
# -- the sum of the odd numbers.
#
# sum_of_evens_and_odds((1, 2, 3, 4))   =&gt; (6, 4)
# sum_of_evens_and_odds((1, 3, 5))      =&gt; (0, 9)
# sum_of_evens_and_odds((2, 4, 6))      =&gt; (12, 0)

#1
def sum_of_evens_and_odds(numbers):
    total_even=0
    total_odd=0
    for num in numbers:
        if num % 2 == 0:
            total_even += num
        else:
            total_odd += num
    return total_even, total_odd
print(sum_of_evens_and_odds((1, 2, 3, 4)))

#2
def sum_of_evens_and_odds(numbers):
    even_num = [num for num in numbers if num % 2 == 0]
    odd_num = [num for num in numbers if num % 2 != 0]
    return sum(even_num), sum(odd_num)

print(sum_of_evens_and_odds((1, 2, 3, 4)))
    