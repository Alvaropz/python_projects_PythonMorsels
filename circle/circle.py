#Python Morsels

import math

class Circle:
    def __init__(self, number=1):
        self.number = self.num_checker(number)

    def __repr__(self):
        return f"Circle({self.number})"

    @property
    def radius(self):
        return self.number

    @property
    def diameter(self):
        d = self.number * 2
        return d

    @property
    def area(self):
        result = math.pi * (self.number ** 2)
        return result

    @radius.setter
    def radius(self, number):
        self.number = self.num_checker(number)

    @diameter.setter
    def diameter(self, number):
        self.number = self.num_checker(number) / 2

    def num_checker(self, number):
        if number < 0:
            raise ValueError("Radius cannot be negative")
        self.number = number
        return self.number