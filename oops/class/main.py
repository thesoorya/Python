from class_file import Car # importing Car class from another file as module

car_1 = Car('Audi', 'R8', 2020, 'Red')
car_2 = Car('BMW', 'Q7', 2020, 'Blue')

# attributes
print(car_1.model)
print(car_1.name)
print(car_1.year)
print(car_1.color)
print(car_1.wheels)

print(car_2.model)
print(car_2.name)
print(car_2.year)
print(car_2.color)

# methods / functions
car_1.about()
car_1.welcome()

# class
print(car_1)
Car(model='Porche', name='911', year=2020, color='yellow')