# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 16:58:53 2021

@author: Praveen
"""

# Define a to_dictionary function that accepts a list of strings. 
# The function should return a dictionary where the keys are the strings 
# and the values are their original index positions in the list.
#
# EXAMPLE:
detectives = ["Sherlock Holmes", "Hercule Poirot", "Nancy Drew"]
# to_dictionary(detectives) => {'Sherlock Holmes': 0, 'Hercule Poirot': 1, 'Nancy Drew': 2}

def to_dictionary(texts):
    dicts = {}
    for idx, value in enumerate(texts):
        dicts[value] = idx
        
    return dicts
print(to_dictionary(detectives))

# Define a length_counts function that accepts a list of strings. 
# The function should return a dictionary where the keys represent
# length and the values represent how many strings have that length.
#
# EXAMPLE:
sa_countries = ["Brazil", "Venezuela", "Argentina", "Ecuador", "Bolivia", "Peru"]
# length_counts(sa_countries) => # {6: 1, 9: 2, 7: 2, 4: 1}
# There is 1 string with 6 letters, 2 strings with 9 letters, 
# 2 strings with 7 letters, and 1 string with 4 letters.

def length_counts(lists):
    dicts = {}
    for value in lists:
        if len(value) in dicts:
            dicts[len(value)] += 1
        else:
            dicts[len(value)] = 1
    return dicts
print(length_counts(sa_countries))

##2
def length_counts(lists):
    dicts = {}
    for value in lists:
        length = len(value)
        count = dicts.get(length,0)
        dicts[length] = count+1
    return dicts
print(length_counts(sa_countries))

####
confusion = {
  "a": "b",
  "b": "c",
  "c": "d"
}
#value = del confusion["b"]
#print(value)
    
####
# Declare a delete_keys function that accepts two arguments:
# a dictionary and a list of strings. 
# For each string in the list, if the string exists as a dictionary key, 
# delete the key-value pair from the dictionary. 
#
# If the string does not exist as a dictionary key, avoid an error. 
# The return value should be the modified dictionary object.
#
# EXAMPLE:
my_dict = {
  "A": 1,
  "B": 2,
  "C": 3
}
#
strings = ["A", "C"]
# delete_keys(my_dict, strings) => {'B': 2}

def delete_keys(dicts, lists):
    
    for value in lists:
        if value in dicts:
            dicts.pop(value)
    return dicts

print(delete_keys(my_dict, strings))
            
    