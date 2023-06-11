# Given a list, write a Python program to swap first and last element of the list.

# Examples: 

# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]

# Input : [1, 2, 3]
# Output : [3, 2, 1]

def swap_first_last(lists:list) -> list:
    lists[0], lists[-1] = lists[-1],lists[0]
    return lists
#examples
input1 = [12, 35, 9, 56, 24]
print(swap_first_last(input1))
input2 = [1, 2, 3]
print(swap_first_last(input2))

# Can also use the list unpacking method: first, *middle, last = [a,b,c,d]
# def swap_first_last(lists:list) -> list:
#     # lists[0], lists[-1] = lists[-1],lists[0]
#     first, *middle, last = lists
#     lists = [last, *middle, first]
#     return lists