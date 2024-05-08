class Animal:
    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

class DogCat(Dog, Cat):
    pass

# Creating an instance of DogCat
dc = DogCat()

# Calling the make_sound method of DogCat
dc.make_sound()