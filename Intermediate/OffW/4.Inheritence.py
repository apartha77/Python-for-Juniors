


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
- Relationship between the classes - 1. Aggregation ( Has-A) 2. Inheritance (Is-A)
- Aggregation - Customer has Address
- Inheritence - Car is a Vehicle
- With inheritence - the class inheriting gets all the 
    - data members (variables),
    - member functions (methods), 
    - constructor
    Cannot inherit the Private members (with __)
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

""" How to inherit constructor --
1. The class can inherit constuctor from base class, child may not have a constructor
2. Child class can't access hidden(private __) members of parent class
3. Polymorphism 
  - method overriding- both can have same method, but child will be called
  - method overloading - doesn't work same as C# - same method with different parameters. Howerver, using default value of parameters achieve method overloading
  - Operator overlaoding - + can be used to concatenate and two numbers, using magic methods __ 
If child has constructor, then parent constructor will not be called.
4. Super() - keyword - to call Parent methods and constructor. 
Super will only work within the class cannot call from outside.
To initialise child and parent constuctor - call super().__init__() within child constructor 
"""
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")
        

class SmartPhone(Phone):
    def buy(self):
        print("Buying a smartphone")
        super().buy() # calling parent method and constructor
    pass


if __name__ == "__main__":
    address1 = Address("Kolkata", 700063, "WB") # object of address
    customer1 = Customer("Test", 47, address1) #object of Customer 
    
    print(customer1.address.pin)
    customer1.edit_profile("Test2",700064)
    print(customer1.name, customer1.address.pin)

    s = SmartPhone(20000, "Apple", 13)
    print(s.brand)
    s.buy()
