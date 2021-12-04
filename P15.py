# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 09:43:04 2021

@author: Praveen
"""

# Declare a right_words function that accepts a list of words and a number.
# Return a new list with the words that have a length equal to the number.
# Do NOT use list comprehension.
#
# EXAMPLES:
# right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 3)     => ['cat', 'dog', 'ace']
# right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 5)     => ['heart']
# right_words([], 4)

def right_words(words,num):
    return filter(lambda word: len(word) == num,words)

print(list(right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 3)))


# Declare an only_odds function.
# It should accept a list of whole numbers.
# It should return a list with only the odd numbers from the original list.
# Do NOT use list comprehension.
#
# EXAMPLES:
# only_odds([1, 3, 5, 6, 7, 8])      =&gt;  [1, 3, 5, 7]
# only_odds([2, 4, 6, 8])            =&gt;  []

def only_odds(nums):
    return list(filter(lambda num: num % 2 != 0,nums))
print(only_odds([1, 3, 5, 6, 7, 8]))
print(only_odds([2, 4, 6, 8]))
print()    


# Declare a count_of_a function that accepts a list of strings.
# It should return a list with counts of how many “a” characters appear per string.
# Do NOT use list comprehension.
#
# EXAMPLES:
# count_of_a(["alligator", "aardvark", "albatross"])    =&gt; [2, 3, 2]
# count_of_a(["plywood"])                               =&gt; [0]
# count_of_a([])  

def count_of_a(letters):
    return list(map(lambda letter: letter.count('a'), letters))

print(count_of_a(["alligator", "aardvark", "albatross"]))
print(count_of_a(["plywood"]) )
print(count_of_a([]) )