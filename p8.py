# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 00:19:33 2021

@author: Praveen
"""

# Declare a length_match function that accepts a list of strings and an integer.
# It should return a count of the number of strings whose length is equal to the number.
#
# EXAMPLES
# length_match(["cat", "dog", "kangaroo", "mouse"], 3))  => 2
# length_match(["cat", "dog", "kangaroo", "mouse"], 5))  => 1
# length_match(["cat", "dog", "kangaroo", "mouse"], 4))  => 0
# length_match([], 5))   

def length_match(lists,target):
    count = 0
    for ele in lists:
        if len(ele) == target:
            count += 1
    return count

print(length_match(["cat", "dog", "kangaroo", "mouse"], 4))

# Declare a sum_from function that accepts two numbers as arguments.
# The second number will always be greater than the first number.
# The function should return the sum of all numbers from the first number to the 
# second number (inclusive).
# EXAMPLES
# sum_from(1, 2)   # 1 + 2                  => 3
# sum_from(1, 5)   # 1 + 2 + 3 + 4 + 5      => 15
# sum_from(3, 8)   # 3 + 4 + 5 + 6 + 7 + 8  => 33
# sum_from(9, 12)  # 9 + 10 + 11 + 12       => 42

def sum_from(num1,num2):
    total = 0
    if num1 < num2:
        for num in range(num1,num2+1):
            total += num
    return total
print(sum_from(3,8))


# Declare a same_index_values function that accepts two lists.
# The function should return a list of the index positions 
# in which the two lists have equal elements
# EXAMPLES
# same_index_values([1, 2, 3], [3, 2, 1])                         => [1]
# same_index_values(["a", "b", "c", "d"], ["c", "b", "a", "d"])   => [1, 3]

def same_index_values(list1,list2):
    idx = []
    for idx1,num1 in enumerate(list1):
        for idx2,num2 in enumerate(list2):
            if num1 == num2 and idx1 == idx2:
                idx.append(idx1)
    return idx
print(same_index_values([1, 2, 3], [3, 2, 1]) )
print(same_index_values(["a", "b", "c", "d"], ["c", "b", "a", "d"]))
                
        
print()
    
def same_index_values(list1,list2):
    idx = []
    for idx1,num1 in enumerate(list1):
        if num1 == list2[idx1]:
            idx.append(idx1)
    return idx
print(same_index_values([1, 2, 3], [3, 2, 1]) )
print(same_index_values(["a", "b", "c", "d"], ["c", "b", "a", "d"]))
                