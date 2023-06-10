# Python program to swap two elements in a list

# Given a list in Python and provided the positions of the elements, 
# write a program to swap the two elements in the list.
 
# Examples:  

#     Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
#     Output : [19, 65, 23, 90]

#     Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
#     Output : [1, 5, 3, 4, 2]

def swap_ele(lists:list, pos1:int, pos2:int) -> list:
    lists[pos1-1], lists[pos2-1] = lists[pos2-1], lists[pos1-1]
    return lists

print(swap_ele([23, 65, 19, 90], 1, 3))
print(swap_ele([1, 2, 3, 4, 5], 2, 5))