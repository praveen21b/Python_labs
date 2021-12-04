# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 23:17:00 2021

@author: Praveen
"""

# Define a word_lengths function that accepts a string. 
# It should return a list with the lengths of each word.
#
# EXAMPLES
# word_lengths("Mary Poppins was a nanny")  => [4, 7, 3, 1, 5]
# word_lengths("Somebody stole my donut")   => [8, 5, 2, 5]

def word_lengths(text):
    new_list = text.split(' ')
    length = []
    for value in new_list:
       length.append(len(value)) 
    return length
print(word_lengths("Mary Poppins was a nanny"))


# Define a cleanup function that accepts a list of strings.
# The function should return the strings joined together by a space.
# There's one BIG problem -- some of the strings are empty or only consist of spaces!
# These should NOT be included in the final string
#
# cleanup(["cat", "er", "pillar"])           => "cat er pillar"
# cleanup(["cat", " ", "er", "", "pillar"])  => "cat er pillar"
# cleanup(["", "", " "])

#1
def cleanup(lists):
    for value in lists:
        if value == '' or value == ' ':
            lists.remove('')
            lists.remove(' ')
    return ' '.join(lists)


print(cleanup(["cat", "er", "pillar"]))
print(cleanup(["cat", " ", "er", "", "pillar"]))
print(cleanup(["", "", " "]))


#2
def cleanup(lists):
    NewList =[] 
    for value in lists:
        if value.isspace() or len(value) == 0:
            continue
        NewList.append(value)
    return ' '.join(NewList)


print(cleanup(["cat", "er", "pillar"]))
print(cleanup(["cat", " ", "er", "", "pillar"]))
print(cleanup(["", "", " "]))




