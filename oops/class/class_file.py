class Car:
   
    # class variable / prototype in js
    # we can create a common variable in class for all instance and also rewrite or modify in main file 
    # like using Class name 
    # eg., Car.wheels = 2 but it also affects the every instance 
    # insted, using the individual object instance like car_1.wheels = 2 it will reflect only in that instance
    wheels = 4
   
    # instance variable
    def __init__(self, model, name, year, color):
        self.model = model
        self.name = name
        self.year = year
        self.color = color
        
    def welcome(self):
        print(f'welcome to {self.model}')
        
    def about(self):
        print(f'{self.name} is good car')
        
    def __str__(self):
        return f"Car(model='{self.model}', name='{self.name}', year={self.year}, color='{self.color}')"