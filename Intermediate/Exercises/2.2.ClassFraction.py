# ============================================================
# Sample        :   OOPS in Python.
# By            :   Partha Das
# Created On    :   20-May-2025
# Last Updated  :   
# Git Repo      :   https://github.com/apartha77/
# ============================================================


# Custom data type - Fraction 
class Fraction:
    def __init__(self, n, d): # while creating object have to provide n, d
        self.num = n
        self.den = d
    """ Use of another magic method __str___ 
    used while printing the class objects
    Another __add__ to add two objects
    """
    def __str__(self):
        return "{}/{}".format(self.num, self.den)

    def __add__(self, other):
        temp_num = self.num * other.den + other.num * self.den
        temp_den = self.den * other.den
        return "{}/{}".format(temp_num, temp_den)
        # add to simplify the fraction and then return.

if __name__ == "__main__":
    a = Fraction(4,5)
    print(type(a))
    print(a)
    b = Fraction(5,3)
    print(a+b)

    #encapsulation
    
