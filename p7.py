# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 12:39:16 2021

@author: Praveen
"""

## For Loop

# Define a sum_of_lengths function that accepts a list of strings.
# The function should return the sum of the string lengths.
#
# EXAMPLES
# sum_of_lengths(["Hello", "Bob"])                  => 8
# sum_of_lengths(["Nonsense"])                      => 8
# sum_of_lengths(["Nonsense", "or", "confidence"])  => 20

def sum_of_lengths(lists):
    length = 0
    for element in lists:
        length += len(element)
    return length
        
print(sum_of_lengths(["Nonsense", "or", "confidence"]))


# Define a product function that accepts a list of numbers.
# The function should return the product of the numbers.
# The list will always have at least one value
#
# EXAMPLES
# product([1, 2, 3])     => 6
# product([4, 5, 6, 7])  => 840
# product([10])          => 10

def product(nums):
    prod = 1
    for num in nums:
        prod *= num
    return prod
print(product([4,5,6,7]))

##
values = [3,6,9,12,15,18,21,24]
other_values = [5,10,15,20,25,30]

def odd_sum(lists):
    total = 0
    for num in lists:
        if not num % 2 == 0:
            total += num
        else:
            continue
    return total

print(odd_sum(values))
print(odd_sum(other_values))


##
def greatest_number(numbers):
    return max(numbers)
print(greatest_number([-3,-2,-1]))

def greatest_number(numbers):
    maxNum = numbers[0]
    for num in numbers:
        if num > maxNum:
            maxNum = num
    return maxNum
print(greatest_number([-3,-2,2]))

######
# Define a concatenate function that accepts a list of strings. 
#
# The function should return a concatenated string which consists of
# all list elements whose length is greater than 2 characters.
#
# concatenate(["abc", "def", "ghi"])      => "abcdefghi"
# concatenate(["abc", "de", "fgh", "ic"]) => "abcfgh"
# concatenate(["ab", "cd", "ef", "gh"])   => ""

def concatenate(lists):
    char = ''
    for ele in lists:
        if len(ele) > 2:
            char += ele
    return char

print(concatenate(["abc", "def", "ghi"]))
print(concatenate(["abc", "de", "fgh", "ic"]))

#######
# Define a super_sum function that accepts a list of strings. 
# The function should sum the index positions of the first occurence of the letter 
#“s” in each word.

# Not every word is guaranteed to have an “s”.
# Don’t use "sum" as a variable name as it’s a built-in keyword.
#
# super_sum([])                                 => 0
# super_sum(["mustache"])                       => 2
# super_sum(["mustache", "greatest"])           => 8
# super_sum(["mustache", "pessimist"])          => 4
# super_sum(["mustache", "greatest", "almost"]) => 12

def super_sum(lists):
    total = 0
    for ele in lists:
        if 's' in ele:
            total += ele.index('s')
    return total
print(super_sum([]))
print(super_sum(["mustache"]))            
print(super_sum(["mustache", "greatest", "almost"]))

##### enumerate function
# Define an in_list function that accepts a list of strings and a separate string.
# Return the index where the string exists in the list.
# If the string does not exist, return -1.
# Do NOT use the find or index methods.
#
# EXAMPLES
# strings = ["enchanted", "sparks fly", "long live"]
# in_list(strings, "enchanted")  ==> 0
# in_list(strings, "sparks fly") ==> 1
# in_list(strings, "fifteen")    ==> -1
# in_list(strings, "love story") ==> -1

strings = ["enchanted", "sparks fly", "long live"]

def in_list(text, target):
    for idx, ele in enumerate(text):
        if ele == target:
            return idx
    return -1
print(in_list(strings, "love story"))
        
# Define a sum_of_values_and_indices function that accepts a list of numbers. 
# It should return the sum of all of the elements along with their index values.
#
# EXAMPLES
# sum_of_values_and_indices([1, 2, 3])    => (1 + 0) + (2 + 1) + (3 + 2) => 9
# sum_of_values_and_indices([0, 0, 0, 0]) => 6
# sum_of_values_and_indices([])           => 0

def sum_of_values_and_indices(lists):
    total = 0
    for idx, ele in enumerate(lists):
        total += (idx+ele)
    return total
print(sum_of_values_and_indices([0, 0, 0, 0]))
print(sum_of_values_and_indices([]))
        

for index, num in enumerate([1, 1, 2, 2, 5]):
  if index < num:
    continue
 
  print(num)
  



