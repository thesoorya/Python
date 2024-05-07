# Slicing and indexing are fundamental operations for accessing elements within data structures like lists, strings, tuples, etc., in Python.

# Indexing refers to accessing individual elements within a data structure using their position, or index. Indexing in Python starts from 0 for the first element, 1 for the second element, and so on.

# Slicing refers to extracting a portion of a sequence (like a list or a string) by specifying a range of indices.

# indexing

name ='soorya narayanan'
# [start, end, step]
print(name[0]) #gives 0th index value
print(name[0: 7]) #gives 0th index to 6th index value because start is inclusive and end is exclusive
print(name[0: : 2]) #gives the every second element in variable

# negative indexing
print(name[0: -2]) #-ve value starts from last index 

# slicing
slice = slice(0,4)
sliced = name[slice]
print(sliced)