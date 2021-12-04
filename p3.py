# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 19:26:34 2021

@author: Praveen
"""

# Define a vowel_count function that accepts a string argument.
# The function should return the count of vowels in the string.
# The 5 vowels are "a", "e", "i", "o", and "u".
# You can assume the string will be in all lowercase.
#
# EXAMPLES:
# vowel_count("estate")        => 3
# vowel_count("helicopter")    => 4
# vowel_count("ssh")           => 0

def vowel_count(name):
    return (name.count('a') + name.count('e') + name.count('i') +name.count('o') + name.count('u'))

print(vowel_count('Praveen'))

# Define a find_my_letter function that accepts two arguments: a string and a character
# The function should return the first index position of the character in the string
# The function should return a -1 if the character does not exist in the string
#
# EXAMPLES:
# find_my_letter("dangerous", "a")    => 1
# find_my_letter("bazooka", "z")      => 2
# find_my_letter("lollipop", "z")     => -1

def find_my_letter(name, char):
    return name.find(char)

print(find_my_letter('dangerous', 'a'))
print(find_my_letter('dangerous', 'b'))


# Define a fancy_cleanup function that accepts a single string argument
# The function should clean up the whitespace on both sides of the
# argument. It should also replace every occurrence of the letter "g" with the
# letter "z" and every occurence of a space with an exclamation point (!).
#
# fancy_cleanup("       geronimo crikey  ")   => "zeronimo!crikey"
# fancy_cleanup("       nonsense  ")          => "nonsense"
# fancy_cleanup("grade")                      => "zrade"

def fancy_cleanup(text):
    return text.strip().replace('g', 'z').replace(' ', '!')

print(fancy_cleanup("       geronimo crikey  "))
