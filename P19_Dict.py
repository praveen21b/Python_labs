# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 17:28:22 2021

@author: Praveen
"""

# Declare an invert function that accepts a dictionary object. 
# The function should return a new dictionary where the keys and values from the original dictionary are inverted. 
# Each key should now be a value, and each value should be a key. 
# Assume both the keys and values of the dictionary are immutable.
#
# EXAMPLE:
my_dict = {
   "A": "B", 
   "C": "D",
   "E": "F"
}
#
# invert(my_dict) => {'B': 'A', 'D': 'C', 'F': 'E'}

## 1
def invert(dicts):
    new = {}
    for key, value in dicts.items():
        new[value] = key
    return new
print(invert(my_dict))

##2
def invert(dicts):
    return {value: key for key, value in dicts.items()}

print(invert(my_dict))

# Declare a count_of_value function that accepts a dictionary and an integer.
# It should return a count of the number of times the integer appears 
# as a value among the dictionary’s values.
#
# EXAMPLE:
my_dict = { "a" : 5, "b" : 3, "c" : 5 }
#
# count_of_value(my_dict, 5) => 2
# count_of_value(my_dict, 3) => 1

def count_of_value(dicts,target):
    count = 0
    for key,value in dicts.items():
        if value == target:
            count += 1
    return count
print(count_of_value(my_dict, 5))
print(count_of_value(my_dict, 3))
print()
print()


# Declare a sum_of_values function that accepts a dictionary and a list of strings.
# The dictionary will have keys of strings and values of numbers.
#
# The function should return the sum of values for dictionary 
# keys that are also found in the list.
#
# NOTE: sum is a reserved keyword in Python. Don’t use it as a variable name.
#
# EXAMPLES:
my_dict = { "a": 5, "b": 3, "c": 10 }
#
# sum_of_values(my_dict, ["a"])            => 5
# sum_of_values(my_dict, ["a", "c"])       => 15
# sum_of_values(my_dict, ["a", "c", "b"])  => 18
# sum_of_values(my_dict, ["z"])            => 0

def sum_of_values(dicts,lists):
    total = 0
    for key,value in dicts.items():
        if key in lists:
            total += value
    return total
print(sum_of_values(my_dict, ["a"]))
print(sum_of_values(my_dict, ["a", "c"]))
print(sum_of_values(my_dict, ["a", "c", "b"]))
print(sum_of_values(my_dict, ["z"]))


# Declare a common_elements function that accepts a dictionary
# It should return a list with all of the elements that are found
# as both a key and a value in the dictionary
#
# HINT: Use the in operation to check for inclusion in a view or list object
#
# EXAMPLE:
my_dict = {
   "A": "K",
   "B": "D",
   "C": "A",
   "D": "Z"
}
#
# common_elements(my_dict) => ["A", "D"]

def common_elements(dicts):
    new = []
    for key in dicts.keys():
        if key in dicts.values():
            new.append(key)
    return new
print(common_elements(my_dict))

print()

# Assign a list of four dictionaries to a "complexity" variable below

# The first and third dictionaries should have two key-value pairs
# For those dictionaries, the keys should be strings and the values should be Booleans

# The second and fourth dictionaries should have three key-value pairs
# For those dictionaries, the keys shoulds be floats and the values should be list of strings. 
# The lists can be of any length.

complexity = [ {"A": True, "B": False},
              {1.0 : [1,2], 2.1 : [3,4,5], 3.2:[6,7]},
              {"C": False, "D": False},
              {1.3 : [1,2,5,6], 2.3 : [3,4,5,4], 3.1:[6,7,7,8]}              
    ]
print(complexity)
print()

# Declare a plenty_of_arguments function that accepts two parameters (a and b)
# and an additional **kwargs parameter.
#
# The function should return True if the sum of a, b, and the values of 
# **kwargs is greater than 100. It should return False otherwise.
#
# EXAMPLES:
# plenty_of_arguments(20, 30)                          => False
# plenty_of_arguments(a = 50, b = 75)                  => True
# plenty_of_arguments(a = 50, b = 25, c = 50)          => True
# plenty_of_arguments(a = 25, b = 25, c = 25, d = 25)  => False
# plenty_of_arguments(a = 25, b = 25, c = 25, d = 26)  => True

def plenty_of_arguments(a,b,**kwargs):
    total = a+b
    for value in kwargs.values():
        total += value
    return total > 100
print(plenty_of_arguments(20, 30))
print(plenty_of_arguments(a = 50, b = 75))
print(plenty_of_arguments(a = 50, b = 25, c = 50) )
print(plenty_of_arguments(a = 25, b = 25, c = 25, d = 25))
print(plenty_of_arguments(a = 25, b = 25, c = 25, d = 26))
print()

def plenty_of_arguments(a,b,**kwargs):
    total = a+b+sum(kwargs.values())
    return total > 100
print(plenty_of_arguments(20, 30))
print(plenty_of_arguments(a = 50, b = 75))
print(plenty_of_arguments(a = 50, b = 25, c = 50) )
print(plenty_of_arguments(a = 25, b = 25, c = 25, d = 25))
print(plenty_of_arguments(a = 25, b = 25, c = 25, d = 26))
print()

sentences = [
  "Bobby went to the store on the corner",
  "Sally ate a candy bar",
  "Justin played on his deluxe piano"
]
print(sentences[0].split(' '))
print(len(sentences[0]) - sentences[0].count(' '))
#for sentence in sentences:
#    sentence.split(' ')
print()

# You are writing a Python program to model a remote control
# for a television set. Declare a stations_to_numbers
# function that accepts a dictionary. The keys will be
# channel numbers and the values will be the station names.
# For example...
channels = {
   2: "CBS",
   4: "NBC",
   5: "FOX",
   7: "ABC"
}
# The stations_to_numbers function should return an
# inverted dictionary where the keys are the station names
# and the values are the channel numbers
#
# stations_to_numbers(channels) => {'CBS': 2, 'NBC': 4, 'FOX': 5, 'ABC': 7}

def stations_to_numbers(dicts):
    return { value: keys for keys, value in dicts.items()}
print(stations_to_numbers(channels))
print()

# Declare a coaster_conversion function that accepts a dictionary
# The keys of the dictionary will be strings representing roller coasters
# The values will be the heights of each coaster in meters
#
# Return a new dictionary with the same keys.
# The values should be the heights converted from meters to feet,
# The final values (in feet) should also be rounded to the closest integer
# HINT: 1 meter is equal to 3.28084 feet
# HINT: The round function rounds a number to the nearest integer
#
coasters = {
   "Kingda Ka": 139,
   "Top Thrill Dragster": 130,
   "Superman: Escape From Krypton": 126
}
#
# coaster_conversion(coasters) => {'Kingda Ka': 456, 'Top Thrill Dragster': 426, 'Superman: Escape From Krypton': 413}
          
def coaster_conversion(dicts):
    return {key: round(value*3.28084) for key, value in dicts.items()}
print(coaster_conversion(coasters))

print(set())
    
    