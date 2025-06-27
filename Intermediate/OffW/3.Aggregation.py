# ============================================================
# Sample        :   OOPS in Python.
# By            :   Partha Das
# Created On    :   20-May-2025
# Last Updated  :   
# Git Repo      :   https://github.com/apartha77/
# ============================================================



"""
Object oriented programming
1. Class
2. Object
3. Inheritence
4. Encapsulation
5. Polymorphism
6. Abstraction
"""

"""
- Reference variable - while creating an object, 
when you keep in a a varible sbi = Atm() where sbi is reference variable 
- Pass by reference - sending object as parameter of a function, essentially sending the reference variable
- Class objects are mutable like list, disct, sets, hence values can change inside a function
- Static variables and methods
- Relationship between the classes - 1. Aggregation ( Has-A) 2. Inheritance (Is-A)
- Aggregation - Customer has Address
- Inheritence - Car is a Vehicle
"""
class Customer:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def edit_profile(self, new_name, new_pin):
        self.name = new_name
        #self.address.pin = new_pin
        self.address.change_address(new_pin)

class Address:
    def __init__(self, city, pin, state):
        self.city = city
        self.pin = pin
        self.state = state

    def change_address(self, new_pin):
        self.pin = new_pin
"""
Pass the Address object to the customer object
Can access values from Address class from object of Customer class
"""


if __name__ == "__main__":
    address1 = Address("Kolkata", 700063, "WB") # object of address
    customer1 = Customer("Test", 47, address1) #object of Customer 
    
    print(customer1.address.pin)
    customer1.edit_profile("Test2",700064)
    print(customer1.name, customer1.address.pin)


