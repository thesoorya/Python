# In Python, data types are used to classify different types of data. Here are some of the common data types in Python:

# 1. **Numeric Types**:
#    - `int`: Integer data type represents whole numbers, such as 5, -3, 100, etc.
#    - `float`: Float data type represents floating-point numbers, such as 3.14, -0.001, 2.0, etc.
#    - `complex`: Complex data type represents complex numbers in the form `a + bj`, where `a` and `b` are floats and `j` is the imaginary unit.

# 2. **Sequence Types**:
#    - `str`: String data type represents a sequence of characters, such as "hello", 'Python', "123", etc.
#    - `list`: List data type represents an ordered collection of items, which can be of different data types. Example: `[1, 2, 3, 'hello']`.
#    - `tuple`: Tuple data type is similar to a list but is immutable (unchangeable). Example: `(1, 2, 3, 'hello')`.

# 3. **Mapping Type**:
#    - `dict`: Dictionary data type represents a collection of key-value pairs. Each key is associated with a value. Example: `{'name': 'John', 'age': 30}`.

# 4. **Set Types**:
#    - `set`: Set data type represents an unordered collection of unique elements. Example: `{1, 2, 3, 4}`.

# 5. **Boolean Type**:
#    - `bool`: Boolean data type represents either True or False, used in boolean operations and expressions.

# 6. **None Type**:
#    - `None`: NoneType represents the absence of a value or a null value.

# These are the fundamental data types in Python. Additionally, there are data structures and modules that can handle more complex data types or specialized data manipulation, such as arrays, datetime objects, etc.


#string data type
name = 'soorya'
print(name)
print(type(name))

#integer data type (int only store's the whole number cannot store the decimal number)
age = 21
age = age + 1 #age +=1 (for increment)
#print('your age is' + age) we cannot concat str with integer
print('your age is ' + str(age)) #need to convert the type to concat
print(age)
print(type(age))

#float data type
height = 173.7
print(height)
print('your height is ' + str(height) + 'cm')
print(type(height))

# boolean data type
student = True
print(student)
print(type(student))
# also works in concat