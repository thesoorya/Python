# Exception handling in Python allows you to deal with unexpected errors that occur during the execution of a program. 

try:
    a = int(input('Enter the number: '))
    b = int(input('Enter the another number: '))
    res = a / b
    print(res)
    
# there are many inbuilt exceptions, but Exception is common way to catch the errors
except Exception as e:
    print(e)
    
# syntax

# try:
#     # Code that might raise an exception
#     # ...
# except ExceptionType1:
#     # Handle ExceptionType1
#     # ...
# except ExceptionType2:
#     # Handle ExceptionType2
#     # ...
# else:
#     # Execute if no exception occurs
#     # ...
# finally:
#     # Execute whether an exception occurs or not
#     # ...