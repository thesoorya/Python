# Inheritance is a fundamental concept in object-oriented programming (OOP) that allows classes to inherit attributes and methods from other classes. In Python, you can create a new class that inherits from an existing class, known as the superclass or parent class. The new class is called a subclass or child class.

class Vechile:
    
    wheels = 4
    
    def type(self):
        print(f'This is a {self.wheels} wheel automobile')
        
class Electric(Vechile):
    def __init__(self, motor):
        self.motor = motor
    
    def engine(self):
        print(f'This is a {self.motor} motor')

class Petrol(Vechile):
    def __init__(self, motor):
        self.motor = motor
    
    def engine(self):
        print(f'This is a {self.motor} motor')
        
car_1 = Petrol('petrol')
car_1.type()
car_1.engine()

print('######')  
     
car_2 = Electric('EV')
car_2.type()
car_2.engine()