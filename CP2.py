# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 14:40:59 2021

@author: Praveen
"""
"""
create a Python program to sort a list in ascending order which starting from the .
left of the list and,compare numbers by pairs. If the first pair is ordered 
[smaller number, larger number], and  so on.
If the first pair is ordered [larger number, smaller number], swap the two 
integers before moving on to the next pair.
then repeat this process again until you get to the end of the list.
Then, return to the beginning of the list and repeats this process again until 
the entire list is sorted.
If the unsorted list is: [5,100,20,15,150,80,210,30], what is the number of swaps 
you will need?
"""

def swap_count(a):
    count = 0
    for i in range(len(a)-1, 0, -1):
        for j in range(i):
            if a[j+1] < a[j]:
                a[j], a[j+1] = a[j+1], a[j]
                count += 1
    print(a)
    return count
            

a = [4,5,1,2,3]
print(a)
#bubSort(numList)
print(swap_count(a))      

#print(number_of_swaps([1,5,100,20,15,150,80,210,30,2]))
#print(number_of_swaps([4,5,1,2,3]))

"""Write a Python program that complete an array with random numbers:"""

from random import randint

def randnum(num):
    return [randint(1,99) for i in range(num)]

print(randnum(4))

"""Create a Python program that takes a number and returns a list with the digits 
of the number in reverse order.
"""

def reverseNum(a):
    return [int(num) for num in str(a)[::-1]]
print(reverseNum(12345))

"""The packing robot  is running the getContainer() function to retrieve the container 
of a product. But something is not right
write a Python program that make the robot perform this packing job:
get_container("Bread") ➞ "bag"
get_container(Beer") ➞ "bottle"
get_container("Candy") ➞ "plastic"
get_container("Cheese") ➞ 'None'
"""
def getContainer(product):
    if product == 'Bread':
        return 'bag'
    elif product == 'Beer':
        return 'bottle'
    elif product == 'Candy':
        return 'plastic'
    elif product == 'Cheese':
        return 'None'
print(getContainer('Bread'))

# using dictionary
container = {'Bread': 'bag', 'Beer': 'bottle', 'Candy': 'plastic', 'Cheese': 'None'}
def getContainer(con,product):
    return con.get(product)
print(getContainer(container,'Bread'))

## Dict indenxing
def getContainer(con,product):
    return con[product]
        
print(getContainer(container,'Bread'))
print()

##empty dict check

def empty_dict(dicts):
    return not dicts

print(empty_dict({}))

"""
Create a Python program that takes a dictionary argument sizes 
(contains width, length, height keys) and returns the volume of the box
"""

def volume(key_value):
    l,w,h = key_value.values()
    return l * w * h

print(volume({'a':5, 'b':5, 'c': 5}))

"""
create a python program with a number and a dictionary with min and max properties, 
return True if the number lies within the given range
"""
def numdict(num, dicts):
    dict_value = dicts.values()
    return min(dict_value) <= num <= max(dict_value)
print(numdict(2,{'a':1, 'b':5, 'c': 5}))
print(numdict(600,{'x':500, 'y':5874, 'z': 560}))

print()

my_dict = {'x':500, 'y':5874, 'z': 560}
print

key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

print('Maximum Value: ',my_dict[key_max])
print('Minimum Value: ',my_dict[key_min])












