# ============================================================
# Sample        :   OOPS in Python.
# By            :   Partha Das
# Created On    :   30-May-2025
# Last Updated  :   
# Git Repo      :   https://github.com/apartha77/
# ============================================================

"""
Understanding for loop
1. Need one Iterable - list, set, 
2. Fetch the Iter (position in Iterable)
3. Use Next method to loop thru until the end
"""

num = [1,2,3,4] #iterable List
# fetch the iterator
it = iter(num)# iterator - now use the next method to fetch the elements
# print(next(it))
# print(next(it))
# print(next(it))

"""
Define your own For loop
"""
def my_for_loop(iterable, type):
    it = iter(iterable)
    print(type)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break
        


b = range(1,11) # range function
c = (1,2,3,4) # tuple
d = {1,2,3,4} # Set
e = {0:1, 1:2, 2:3, 3:4} # dictionary

my_for_loop(num, "List")
my_for_loop(b, "Range")
my_for_loop(c, "Tuple")
my_for_loop(d, "Set")
my_for_loop(e, "Dictionary")



"""
Implementing For loop in our own class
"""
class MyOwnForLoop:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.x = 0
        return self

    def __next__(self):
        x = self.x
        if x >= self.limit:
            raise StopIteration
        self.x = x + 1
        return x









