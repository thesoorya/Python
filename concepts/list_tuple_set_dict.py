# list = array(js) uses- []
# tuple = immutable / unchangable uses- ()
# set = unordered and unindexed use- {}
# dictionaries = objects(js) uses- {}

food = ['pizza', 'burger', 'donet', 'fries']
# print(food)

# food.append('jelly') # add the element at last index
# food.pop() # removes the element at last index
# food.remove('pizza') # removes the element by its value
# food.insert(1, 'cake') # insert the value by its index
# food.sort() # sort by alphabetic order
# food.clear() # clears the list

# for i in food:
#     print(i)

# 2D lists

drinks = ['tea', 'coffee', 'juice']
items = [food, drinks]
print(items)
print(items[0][1]) #to get the value form 2d lists

#############################################################################

# tuples - which is ordered and unchangable used to group togeather related data

tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
tuple3 = (1, 'hello', [4, 5, 6])

# Accessing elements of a tuple
print(tuple1[0])  
print(tuple2[2])  
print(tuple3[1])  

# Tuples are immutable
# tuple1[0] = 10  # This will result in an error because tuples cannot be modified after creation

# Nested tuples
nested_tuple = (1, (2, 3), ('a', 'b', 'c'))

# Tuple unpacking
x, y, z = tuple2
print(x)  
print(y)  
print(z)  

# Length of a tuple
print(len(tuple1))  

# Tuple concatenation
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple) 

#################################################################################

# sets - set is a collection data type that is unordered, mutable, and does not allow duplicate elements. 

set1 = {1, 2, 3}
set2 = {'a', 'b', 'c'}
set3 = {1, 2, 'hello'}

# Sets automatically remove duplicates
set_with_duplicates = {1, 2, 3, 1, 2}
print(set_with_duplicates)  # Output: {1, 2, 3}

# Accessing elements of a set
for element in set1:
    print(element)

# Adding elements to a set
set1.add(4)
print(set1)  # Output: {1, 2, 3, 4}

# Removing elements from a set
set1.remove(2)
print(set1)  # Output: {1, 3, 4}

# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union
union_set = set_a | set_b  # or set_a.union(set_b)
print(union_set)  # Output: {1, 2, 3, 4, 5, 6}

# Intersection
intersection_set = set_a & set_b  # or set_a.intersection(set_b)
print(intersection_set)  # Output: {3, 4}

# Difference
difference_set = set_a - set_b  # or set_a.difference(set_b)
print(difference_set)  # Output: {1, 2}

# Symmetric difference
symmetric_difference_set = set_a ^ set_b  # or set_a.symmetric_difference(set_b)
print(symmetric_difference_set)  # Output: {1, 2, 5, 6}

############################################################################

# dictionaries -  a dictionary is a collection data type that stores key-value pairs. It is unordered, mutable, and does not allow duplicate keys.

# Creating dictionaries
student = {'name': 'John', 'age': 25, 'grade': 'A'}
employee = {101: 'Alice', 102: 'Bob', 103: 'Charlie'}

# Accessing elements of a dictionary
print(student['name'])  # Output: 'John'
print(employee[102])    # Output: 'Bob'

# Adding or modifying elements in a dictionary
student['age'] = 26     # Modifying existing value
student['city'] = 'New York'  # Adding new key-value pair
print(student)          # Output: {'name': 'John', 'age': 26, 'grade': 'A', 'city': 'New York'}

# Removing elements from a dictionary
del student['grade']
print(student)          # Output: {'name': 'John', 'age': 26, 'city': 'New York'}

# Dictionary operations
# Length of a dictionary
print(len(student))    # Output: 3

# Checking if a key exists in a dictionary
print('name' in student)   # Output: True

# Iterating over keys, values, or items (key-value pairs) of a dictionary
for key in student:
    print(key, student[key])

for value in student.values():
    print(value)

for key, value in student.items():
    print(key, value)