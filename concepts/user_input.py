# getting input from user using input keyword

name = input('Enter your name: ')
print('Hello ' + name)

age = int(input('Enter your age: ')) # convert into int because the input getting in number. it applies for float also
print('Your age is ' + str(age))

height = float(input('Enter your height: '))
print('Your height is ' + str(height)  + 'cm')

print(type(input))