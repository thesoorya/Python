# multi-level inheritance when a derived(child) class inherit derived another(child) class

class Organism: 
    alive = True
    
class Animal(Organism):
     def eat(self):
         print('This animals eat')
         
class Dog(Animal):
    def __init__(self, name):
        self.name = name
        
    def bark(self):
        print(f'{self.name} wil bark')
        
dog_1 = Dog('lab')
dog_1.bark()
dog_1.eat()