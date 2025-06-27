# ============================================================
# Sample        :   OOPS in Python.
# By            :   Partha Das
# Created On    :   20-May-2025
# Last Updated  :   
# Git Repo      :   https://github.com/apartha77/
# ==========================================================


"""
Object oriented programming
1. Class
2. Object
3. Inheritence
4. Encapsulation
5. Polymorphism
6. Abstraction
"""

# create a atm class
# Function vs Method - [method is inside a class, functions are defined general]
class Atm:
    """
    - Class and Objects
    - Constructor
    Constructor - is a magic method in python identified by __method__
    The object of a class cannot call magic method, but will be trigerred automatically
    Inside construction - you manage config related tasks may be required
    by the objects. 
    Variables inside constructor are called instance variables. 
    """
    def __init__(self):
        self.pin = ""
        self.balance = 0
        print(id(self))
        self.menu()
        
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
        self.pin = user_pin
      
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


