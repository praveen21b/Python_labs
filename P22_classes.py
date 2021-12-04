# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 00:27:17 2021

@author: Praveen
"""

# Declare a Musical class that accepts a name parameter. 
# In the initialization process for an object, assign the
# name parameter to a name attribute on the object.
#
# Instantiate a Musical object with the name “Rent” 
# and assign it to an “rent" variable.
#
# Instantiate a second Musical object with the name “Book of Mormon" 
# and assign it to a “mormon” variable.
#
# Instantiate a third object from the class with the name “Chicago" 
# and assign it to a “chicago” variable.

class Musical():
    def __init__(self, name):
        self.name = name
        
rent = Musical('Rent')
mormon = Musical('Book of Mormon')
chicago = Musical('Chicago')


## Instance Method

# Declare a Musician class that accepts age and income parameters. 

# In the instantiation process for an object, assign the two parameters
# to two attributes with the same name.

# Declare an enter_club instance method. 
# If the musician is less than 21 years old, the method should 
# return the string "Access denied!”. 
# If the musician is 21 or older, the method should
# return the string "Access granted!".

# Declare a play_show instance method. The method should
# increment the musician’s income by 5.

# EXAMPLES
#
class Musician():
    def __init__(self,age,income):
        self.age = age
        self.income = income
        
    def enter_club(self):
        if self.age < 21:
            return 'Access Denied!'
        return 'Access granted!'
        
    def play_show(self):
        self.income += 5
        
cliff = Musician(age = 27, income = 0)
print(cliff.age)    # 27
print(cliff.enter_club())  # "Access granted!"
print(cliff.income) # 0
cliff.play_show()
print(cliff.income) # 5
cliff.play_show()
print(cliff.income) # 10

# book.py

# Let’s say we want to model a Book as a Python object. 
# A Book has an author and a publisher, which are characteristics that cannot change. 
# A Book also has a page_count, which could be altered if you rip some pages from the book.

# Declare a Book class that accepts author, publisher, and page_count parameters. 
# Each of the parameters should be assigned to an attribute. 
# The author and publisher attributes should be designated as protected (use an underscore). 
# The page_count attribute should be designated public.

# Define a copyright instance method that returns a string with information about the copyright. 
# It should look the string below, where “Grant Cardone” is the value of the protected
# author attribute and “10X Enterprises” is the value of the protected publisher attribute.

# => Copyright Grant Cardone, 10X Enterprises

# The public page_count attribute can always be manually modified. 
# However, we can still define an instance method that modifies it. 

# Declare a rip_in_half instance method. 
# If the book has more than 1 page, it should halve the page_count. 
# If the book has 1 page or less, it should set the page_count to 0.

# See sample execution below
class Book():
    def __init__(self, author, publisher, page_count):
        self._author = author
        self._publisher = publisher
        self.page_count = page_count
        
    def copyright(self):
        #self._author = 'Grant Cardone'
        #self._publisher = '10X Enterprises'
        return f'Copyright {self._author}, {self._publisher}'
    
    def rip_in_half(self):
        if self.page_count > 1:
            self.page_count /= 2
        else:
            self.page_count = 0
            
print()

book = Book(author = "Grant Cardone", publisher = "10X Enterprises", page_count = 10)

print(book.copyright()) # Copyright Grant Cardone, 10X Enterprises

print(book.page_count) # 10
book.rip_in_half()
print(book.page_count) # 5.0
book.rip_in_half()
print(book.page_count) # 2.5
book.rip_in_half()
print(book.page_count) # 1.25
book.rip_in_half()
print(book.page_count) # 0.625
book.rip_in_half()
print(book.page_count) # 0
book.rip_in_half()
print(book.page_count) # 0


