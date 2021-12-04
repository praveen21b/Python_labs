# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 12:36:43 2021

@author: Praveen
"""

"""
Create a Python program that takes a dictionary as an argument and returns a 
string with facts about the city. The city facts will need to be extracted from 
the dictionaries three properties:
name
population
continent
The string should have the following format: X has a population of Y and is situated 
in Z (where X is the city name, Y is the population and Z is the continent the city 
is present in).
"""
def city(dicts):
    city, population, continent = dicts.values()
    return f"{city} has a population of {population} and is situated in {continent}"

print(city({'city': 'Bengaluru', 'population': 100_000_000, 'continent': 'Asia'}))

###2
def city_facts(city):
    return "{} has a population of {} and is situated in {}".format(city['name'],
city['population'], city['continent'])
print(city_facts({'name': 'Bengaluru', 'population': 100_000_000, 'continent': 'Asia'}))


"""
Write a Python program that creates a dictionary with each (key, value) pair being 
the (lower case, upper case) versions of a letter.
"""
def lower_upper(letters):
    return {letter.lower(): letter.upper() for letter in letters}
print(lower_upper('PraveeN'))



"""
Create a Python program that takes a list of dictionaries and returns the 
sum of budgeting for customers in a bank.
"""
def sum_budget(dicts):
    
    return sum(dicts.values())

print(sum_budget({'name': 100, 'b': 200, 'c': 500}))

def get_budgets(x):
    return sum(i['budget'] for i in x)
print(get_budgets([{'budget': 100}, {'budget': 200}, {'budget': 500}]))


"""
Create a Python program that takes a dictionary of students and returns 
a list of student names in alphabetical order.
"""
def alp_order(dicts):
    
    return sorted(dicts.values())

print(alp_order({1:'Praveen', 2:'Prashant',3:'Pragati'}))


"""
Given an list of scrabble tiles (as dictionaries), create a function that outputs 
the maximum possible score a player can achieve by summing up the total number of 
points for all the tiles in their hand. Each hand contains 7 scrabble tiles.
Here's an example hand:
[ { "tile": "N", "score": 1 },
  { "tile": "K", "score": 5 },
  { "tile": "Z", "score": 10 },
  { "tile": "X", "score": 8 },
  { "tile": "D", "score": 2 },
  { "tile": "A", "score": 1 },
  { "tile": "E", "score": 1 }]
The player's maximum_score from playing all these tiles would be 
1 + 5 + 10 + 8 + 2 + 1 + 1, or 28.
"""
def total_score(lists):
    total = 0
    for name in lists:
        print(name)
        total += name['score']
    return total
        
        
        
a =[ { "tile": "N", "score": 1 },
  { "tile": "K", "score": 5 },
  { "tile": "Z", "score": 10 },
  { "tile": "X", "score": 8 },
  { "tile": "D", "score": 2 },
  { "tile": "A", "score": 1 },
  { "tile": "E", "score": 1 }]

print(total_score(a))



"""
Write a Python program that takes a string and calculates the number of 
letters and digits within it. Return the result in a dictionary.
Try it for "Python is the number 1 modern language from 4 programming languages"

"""
char_inp ="Python is the number 1 modern language from 4 programming languages"

def num_str_dgts(char):

  return {
    'LETTERS': sum(1 for x in char if x.isalpha()),
    'DIGITS': sum(1 for x in char if x.isnumeric()),
  }
   
print(num_str_dgts(char_inp))
print()

def num_str_dgts(char):
    count_alp = 0
    count_num = 0
    for ele in char:
        #print(ele)
        if (ele.isalpha()):
            count_alp +=1
        elif (ele.isnumeric()):
            count_num +=1
    return{'Letters': count_alp, 'Digits': count_num}

print(num_str_dgts(char_inp))
print()

"""
Create a function that returns the frequency distribution of a list. 
This function should return an object, where the keys are the unique elements 
and the values are the frequency in which those elements occur.
As following:
get_frequencies(["A", "B", "A", "A", "A"]) ➞ { "A" : 4, "B" : 1 }
"""
import numpy as np

def get_frequencies(lists):
    
    new = np.unique(lists)
    #print({new[0]:lists.count(new[0])})
    return {ele:lists.count(ele) for ele in new}
        
print(get_frequencies(["A", "B", "A", "A", "A"]))
print()

##2

def get_frequencies(fs):
    return {x:fs.count(x) for x in fs}
print(get_frequencies(["A", "B", "A", "A", "A"]))

print()

"""
You work for a manufacturer, and have been asked to calculate the total 
profit made on the sales of a product. You are given a dictionary containing 
the cost price per unit (in dollars), sell price per unit (in dollars), and 
the starting inventory. Return the total profit made, rounded to the nearest dollar. 
Assume all of the inventory has been sold, as following:
profit({ "cost_price": 32.67, "sell_price": 45.00, "inventory": 1200}) ➞ 14796
"""

def profit(info):
    return round((info["inventory"])*(info["sell_price"] - info["cost_price"]))
print(profit(({ "cost_price": 32.67, "sell_price": 45.00, "inventory": 1200})))

"""
Write a Python program that returns True if a dictionary contains the 
specified key, and False otherwise.
"""
a= { "A" : 4, "B" : 1 }
def is_present(dicts,ele):
    return ele in dicts
print(is_present(a,'a'))

"""
Create the instance attributes full name and email in the Employee class. 
Given a person's first and last names:
Form the full name by simply joining the first and last name together, 
separated by a space.
Form the email by joining the first and last name together with a "." 
in between, and follow it with 'company.com' at the end. Make sure everything is in 
lowercase, as following:
empl_1 = Employee("John", "William")
empl_2 = Employee("Sara",  "Michel")
empl_3 = Employee("Suzy", "David")
"""
class Employee():
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.fullname = first + ' ' + last
        #self.email = (first+'.'+last+'@comapany.com').lower()
        #self.email = f'{first} .{last}@comapany.com'.lower()
        self.email = '{}.{}@company.com'.format(first, last).lower()
        

empl_1 = Employee("John", "William")
empl_2 = Employee("Sara",  "Michel")
empl_3 = Employee("Suzy", "David")
print(empl_1.email)
print(empl_1.fullname)

"""
Create a Python program which takes a list of objects from the class IceCream 
and returns the sweetness value of the sweetest iceCream.
Sweetness is calculated from the flavor and number of sprinkles. 
Each sprinkle has a sweetness value of 1, and the sweetness values for the 
flavors are as follows:
Flavours    Sweetness Value
Plain                        0
Vanilla                  5
ChocolateChip 5
Strawberry         10
Chocolate         10
You'll be given instance attributes in the order flavor, num_sprinkles.
ice1 = IceCream("Chocolate", 13)         // value = 10+13 =23
ice2 = IceCream("Vanilla", 0)           // value = 0+5 =5
ice3 = IceCream("Strawberry", 7)        // value = 10 +7=17
ice4 = IceCream("Plain", 18)             // value = 0+18 =18
ice5 = IceCream("ChocolateChip", 3)      // value = 5+3= 8

self.Plain = 0
        self.Vanilla = 5
        self.ChocolateChip = 5
        self.Strawberry = 10
        self.Chocolate=10

"""

class IceCream:
    

    def __init__(self,a):
        self.a = a
        
        
    def compare(self,name,num):
        if name in self.a.keys():
           return a[name]+num
            
a = {'Plain': 0, 'Vanilla': 5,'ChocolateChip': 5, 'Strawberry': 10,'Chocolate': 10} 
      
ice1 = IceCream(a)
print()
print(ice1.a.keys())
print(ice1.compare('Vanilla',5))
print()

"""
Suppose you have a guest list of students and the country they are from, 
stored as key-value pairs in a dictionary. 
GUEST_LIST = { "Emmma": "Germany", "Adalene": "France", "shushin": "Japan", "Robert": "England", "Tamer": "Egypt"} 
Write a Python program that takes in a name and returns a name tag, 
that should read: "Hi! I'm [name], and I'm from [country]."
"""

def name_tag(name):
    GUEST_LIST = { "Emma": "Germany", "Adalene": "France", "shushin": "Japan", "Robert": "England", "Tamer": "Egypt"} 
    if name in GUEST_LIST:
        return f"Hi! I'm {name}, and I'm from {GUEST_LIST[name]}."
    return 'Hi, I am a guest!'

print(name_tag('Emma'))
print()

"""
Given a dictionary of some items with star ratings and a specified star rating, 
return a new dictionary of items which match the specified star rating. 
Return "No results found" if no item matches the star rating given, as following
filter_by_rating({
  "Watermelon" : "*****",
  "Apple" : "****",
  "Grapes" : "*****",
  "Tomato" : "***"}, "*****")
➞ {  "Watermelon" : "*****","Grapes" : "*****"}
    
"""
def filter_rate(dicts, rate):
    new = {}
    for key, value in dicts.items():
        if rate == value:
            new[key] = value
        
    if len(new) != 0:
        return new
    return "No results found"
print()

###2
def filter_by_rating(dicts, rate):
    new = {}
    for key, value in dicts.items():
        if rate == value:
            new[key] = value
    return new or "No results found"

print(filter_by_rating({
  "Watermelon" : "*****",
  "Apple" : "****",
  "Grapes" : "*****",
  "Tomato" : "***"}, "*****"))
print()
print(filter_by_rating({
  "Watermelon" : "*****",
  "Apple" : "****",
  "Grapes" : "*****",
  "Tomato" : "***"}, "*******"))
print()
##3

def filter_by_rating(d, rating):
    return {k:v for k,v in d.items() if d[k]==rating} or 'No results found'
print(filter_by_rating({
  "Watermelon" : "*****",
  "Apple" : "****",
  "Grapes" : "*****",
  "Tomato" : "***"}, "*******"))
print()


"""
Create a function that takes a list of dictionaries (groceries) which 
calculates the total price and returns it as a number. 
A grocery dictionary has a product, a quantity and a price, for example:
{
  "product": "Milk",
  "quantity": 1,
  "price": 2
}
"""
a = [{
  "product": "Milk",
  "quantity": 2,
  "price": 2
},
     {
  "product": "Milk",
  "quantity": 1,
  "price": 12
}]

def total_price_groce(lists):
    total = 0
    for ele in lists:
        total = total + (ele['price']) *ele['quantity']
    return total
print(total_price_groce(a))

print()
### 2
def total_price_groce(lists):
    
    return (sum(ele['price'] *ele['quantity'] for ele in lists))
print(total_price_groce(a))

"""
Create a function that takes a dictionary and returns the keys and 
values as separate lists.
"""
def keys_and_values(d):
  return list(map(list, zip(*sorted(d.items()))))

print(keys_and_values({
  "product": "Milk",
  "quantity": 1,
  "price": 12
}))

##2
def keys_and_values(d):
    return [[keys for keys in d.keys()], [values for values in d.values()]]
print()
print(keys_and_values({
  "product": "Milk",
  "quantity": 1,
  "price": 12
}))
    











