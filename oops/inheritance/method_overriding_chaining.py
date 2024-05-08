# Method overriding occurs when a subclass provides a specific implementation of a method that is already defined in its superclass. This allows subclasses to customize the behavior of inherited methods.

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):  # Method overriding
        print("Dog barks")

dog = Dog()
dog.speak()  # Output: "Dog barks"

# Method chaining is a programming technique where multiple methods can be called on the same object in a single statement. This is achieved by having each method return the object itself (usually referred to as self in Python), allowing subsequent method calls to be chained together.

class Calculator:
    def __init__(self, value):
        self.value = value

    def add(self, x):
        self.value += x
        return self

    def subtract(self, x):
        self.value -= x
        return self

    def multiply(self, x):
        self.value *= x
        return self

# Example of method chaining
result = Calculator(10).add(5).subtract(3).multiply(2).value
print(result)  # Output: 24