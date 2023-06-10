# Swap elements in String list

# Sometimes, while working with data records we can have a problem 
# in which we need to perform certain swap operation in which we 
# need to change one element with other over entire string list. 
# This has application in both day-day and data Science domain. 
# Lets discuss certain ways in which this task can be performed. 

def method_replace(lst:list) -> list:
    new_list = []
    for element in lst:
        element = element.replace('G','-').replace('e','G').replace('-','e')
        new_list.append(element)    
    return new_list

print(method_replace(['Gfg', 'is', 'best', 'for', 'Geeks']))