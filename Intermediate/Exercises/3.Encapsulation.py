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
    - Need for encapsulation
    - Private attributes
    - Getter and Setter Methods
    - Class diagram
    """
# create a atm class
# Function vs Method - [method is inside a class, functions are defined general]
class Atm:
    """
    Variables inside constructor are called instance variables.
    These are available to all the objects of that class
    In C# there are access modifier as public or private 
    similarly in python to make prive put __ example sel.__pin =
    Even the methods can be hidden or made private using __ before the methods
    Nothing in python is truely private - when used with __ it adds
    _Class__variable or method.
    The private variables are access to get set methods, where you have
    control on what you will allow to change. 
    """
    def __init__(self):
        self.__pin = ""
        self.__balance = 0
        print(id(self))
        self.menu()
    
    def get_pin(self):
        return self.__pin
    
    def set_pin(self, new_pin):
        if type(new_pin)==str:
            self.__pin = new_pin
            print("pin changed")
        else:
            print("not allowed")


    def menu(self):
        user_input = input("""
        Hi! How can I help you?
        1. Press 1 to create pin
        2. Press 2 to change pin
        3. Press 3 to check balance
        4. Press 4 to withdraw
        5. Anything else to exit
        """)

        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.change_pin()
        elif user_input == "3":
            self.check_balance()
        elif user_input == "4":
            self.withdraw()
        else:
            exit()

    def create_pin(self):
        user_pin = input("Enter your pin: ")
        self.__pin = user_pin
      
        print("Pin created successfully")
        self.menu()

    def deposit(self):
        self.menu()
        pass


"""
Encapsulation
1. Private variables
2. Public variables
3. Protected variables
4. Object Introspection
5. Getter and Setter

"""


if __name__ == "__main__":
    sbi = Atm()
    print(id(sbi))
    hdfc = Atm()
    print(id(hdfc))


