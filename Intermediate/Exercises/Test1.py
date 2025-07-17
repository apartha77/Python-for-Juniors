# ============================================================
# Sample        :   Day 00 - Write a program that can multiply 2 numbers provided by the user without using the * operator
# By            :   Partha Das
# Created On    :   22-May-2025
# Last Updated  :   
# Git Repo      :   https://github.com/apartha77/Python-for-Juniors
# ============================================================
"""
Write a program that can multiply 2 numbers provided by the user without using the * operator
"""

# Take input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Initialize the result to 0
result = 0

# Use a loop to add num1 to itself num2 times
for i in range(num2):
    result += num1

# Print the result
print("The result of multiplying", num1, "and", num2, "is:", result)
