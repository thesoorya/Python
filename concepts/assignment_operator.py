# In Python, you can assign multiple variables in a single line using a process called "multiple assignment" 

name = 'soorya'
age = 21
student = True

# or

name , age, student = 'name', 21, True

print(name)
print(age)
print(student)

# assigning multiple variable to one value

a = b = c = d = 10

print(a) 
print(b) 
print(c) 
print(d) 

# swapping

x = 20
y = 30

x,y = y,x
print('x : ' + str(x))
print('y : ' + str(y))