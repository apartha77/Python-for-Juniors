# ============================================================
# Sample        :   100 Days of Python.
# By            :   Partha Das
# Created On    :   20-May-2025
# Last Updated  :   
# Git Repo      :   https://github.com/apartha77/
# ============================================================

# Lists
L1 = [1, 2, 3, 4, 5, 6, 7]
print(L1)
# Multi-Dimenstional Lists - 2D, 3D lists
L2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(L2)
# List from words
L3 = list("Kolkata")
print(L3)
# List from range
L4 = list(range(10))
print(L4)
print(L4[::-1])
# Add List items - append(), extend(), insert()
# Delete list items - del(), remove(), pop(), clear()
# List operations - contact, multiply, loop, membership, iteration
# List Functions - len(), max(), min(), sum(), sorted(), index(), count()
# List Comprehension
L5 = [i for i in range(10)]
print(L5)
# memory location - id
print(id(L5))
print(id(L4))
# Memory and Variable reference - call by object reference, aliasing, referencing counting - getrefcount()
# garbase collection, weird - 
# Higher order function - with lambda function

def return_sum(func, L): # taking function and variable as parameter
    result = 0
    for i in L: # loop thru the items in list
        if func(i): # if the function returns true than add the values. Same function used for multiple operation
            result = result + i
    return result    

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x = lambda a: a % 2 == 0 # lambda function to check if the number is even
y = lambda a: a % 2 != 0 # lambda function to check if the number is odd
z = lambda a: a % 3 # lambda function to check if the number is divisible by 3

print(f"Add if even number", return_sum(x, L))
print(f"Add if odd number",return_sum(y, L))
print(f"Add if divisible by 3",return_sum(z, L))
# List comprehension
L = [i for i in range(10)]
# Map, Filter,
# Redue --> import functool ; functools.reduce(lambda x,y: x if x>y else y, L)

