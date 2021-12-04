# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 00:40:11 2021

@author: Praveen
"""

# Nested Lists.


# Define a nested_sum function that accepts a list of lists of numbers
# The function should return the sum of the values
# The list may contain empty lists
#
# EXAMPLES
# nested_sum([[1, 2, 3], [4, 5]])            => 15
# nested_sum([[1, 2, 3], [], [], [4], [5]])  => 15
# nested_sum([[]])                           => 0

def nested_sum(nums):
    total = 0
    for num in nums:
        if num == []:
            continue
        for value in num:
            if value == []:
                continue
            total += value
    return total

print(nested_sum([[1, 2, 3], [4, 5]]))
print(nested_sum([[1, 2, 3], [], [], [4], [5]]))
print(nested_sum([[]]))


# Define a fancy_concatenate function that accepts a list of lists of strings
# The function should return a concatenated string
# The strings in a list should only be concatenated if the length of the list is 3
#
# EXAMPLES
# fancy_concatenate([["A", "B", "C"]])                        => "ABC"
# fancy_concatenate([["A", "B", "C"], ["D", "E", "F"]])       => "ABCDEF"
# fancy_concatenate([["A", "B", "C"], ["D", "E", "F", "G"]])  => "ABC"
# fancy_concatenate([["A", "B", "C"], ["D", "E"]])            => "ABC"
# fancy_concatenate([["A", "B"], ["C", "D"]])                 => ""

def fancy_concatenate(lists):
    new = ''
    for value in lists:
        if len(value) == 3:
            for ele in value:
                new += ele
    return new
print(fancy_concatenate([["A", "B", "C"]]))
print(fancy_concatenate([["A", "B", "C"], ["D", "E", "F"]]) )
print(fancy_concatenate([["A", "B", "C"], ["D", "E", "F", "G"]]))
print(fancy_concatenate([["A", "B", "C"], ["D", "E"]]))
print(fancy_concatenate([["A", "B"], ["C", "D"]]))


# Declare a destroy_elements function that accepts two lists.
# It should return a list of all elements from the first list that are NOT contained in the second list.
# Use list comprehension in your solution.
#
# EXAMPLES
# destroy_elements([1, 2, 3], [1, 2])      =&gt; [3]
# destroy_elements([1, 2, 3], [1, 2, 3])   =&gt; []
# destroy_elements([1, 2, 3], [4, 5])      =&gt; [1, 2, 3]

def destroy_elements(ls1,ls2):
     return [ ele for ele in ls1 if ele not in ls2]

print(destroy_elements([1, 2, 3], [1, 2]) )
print(destroy_elements([1, 2, 3], [1, 2, 3]))
print(destroy_elements([1, 2, 3], [4, 5]))