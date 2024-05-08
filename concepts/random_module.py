import random

# random.random() provides random number btw 0 and 1 in decimal form
x = random.random() 
print(x)

# random.randint(1, 5) we need to provide the range from one num to another 
y = random.randint(1,6)
print(y)

# random.choices() uses in any form of collection
list = ['rock', 'paper', 'scissors']
z = random.choice(list)
print(z)

# random.shuffle() it shuffles the collection
list2 = [1,2,3,4,5,6,7,8,9,0]
a = random.shuffle(list2)
print(list2)

# random.smaple() provides 2 unique elements from collection
items = ['apple', 'banana', 'cherry', 'date']
sampled_items = random.sample(items, 2)
print(sampled_items)
