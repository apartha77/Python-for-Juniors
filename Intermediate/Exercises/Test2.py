# ============================================================
# Sample        :   Day 02 - Cover constructure, __init__(), self, encapsulatin, instance metho, instance attributes vs class attributes
# By            :   Partha Das
# Created On    :   06-Jul-2025
# Last Updated  :   
# Git Repo      :   https://github.com/apartha77/Python-for-Juniors
# ============================================================
"""
Wrie a Car class with constuctor, self, encapsulation, instance method, instance attributes, class attributes
1. instance attributes vs class attributes
"""
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand # instnce attribute
        self.model = model # instance attribute
        self.year = year # instnace attribute
    
    vehicle_type = " petrol car" # class attribute 


car1 = Car("maruti", "zen", 2020)
car2 = Car("tata", "nano", 2022)
print(car1.brand, car1.model, car1.year, Car.vehicle_type)
print(car2.brand, car2.model, car2.year, Car.vehicle_type)

print(car1.vehicle_type) # print class attributes
print(car2.vehicle_type)

# Change the class attributes
Car.vehicle_type = "electric car"
print(car1.vehicle_type)

inner-source portal
