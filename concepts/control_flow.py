# # Control flow in programming refers to the order in which statements are executed in a program.

# # if statement

# name = input('Enter your name: ')
# age = int(input('Enter your age: '))

# if age >= 18:
#     print('You are eligible to get license')
# elif age < 18:
#     print('Invalid')
# else:
#     print('You age is not enough')

# # loops

# # while - unlimited
# # for - limited

# # while loop
# # a statement that will execute its block of code remains true

# f_name = None
# while not(f_name): 
#     f_name = input("Enter your name: ")

# print(f_name)

# # for loop
# # a statement runs until the condition is true

# for i in range(10 + 1): #range(start, stop, step)
#     print(i)
    
# for i in range(11, 22):
#     print(i)

# import time

# for i in range(10, 0, -1):
#      print(i)
#      time.sleep(1)
     
# print('Boom')

# loop control statements
# break

while True:
    name2 = input('Enter your name: ')
    if name2 != "":
      break;
  
# continue
# pass