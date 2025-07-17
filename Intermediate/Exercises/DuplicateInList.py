# ============================================================
# Sample        :   Day 00 - Write a python program to remove all the duplicates from a list
# By            :   Partha Das
# Created On    :   22-May-2025
# Last Updated  :   
# Git Repo      :   https://github.com/apartha77/Python-for-Juniors
# ============================================================

"""
Write a python program to remove all the duplicates from a list
"""
L = [1, 2, 3, 1, 2]  # Define a list with duplicates
# easy way to convert to a set and back to a list
L1 = list(set(L))  # Convert the list to a set to remove duplicates, then back to a list
print(L1)  # Print the list without duplicates

# Another way to remove duplicates without converting to a set
L2 = []  # Initialize an empty list to store unique elements
for i in L:
    if i not in L2:
        L2.append(i)  # If the element is not in the new list, append it
print(L2)  # Print the list without duplicates