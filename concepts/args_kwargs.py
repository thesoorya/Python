# *args (Arbitrary Arguments):
# It is used to pass a variable-length argument list to the function.
# The *args parameter is a tuple that allows you to pass any number of positional arguments to a function.

def args(*args):
    res = 0
    
    # args[0] = 0 this will gives error because these are packed with tuple. tuples are immutable / unchnagable
    # args = list(args) this is the way to change the value of the element by type casting to list()
    
    for arg in args:
        res = res + arg
    return res
    
print(args(1,2,3,4))

# **kwargs (Arbitrary Keyword Arguments):
# It is used to pass a variable-length dictionary of arguments to the function.
# The **kwargs parameter is a dictionary that allows you to pass any number of keyword arguments to a function.

def kwargs(**kwargs):
    
    print(kwargs['name'] +' '+ str(kwargs['age']) +' '+ str(kwargs['student'])) # this is the way to access the value by key
    
    for key, value in kwargs.items():
        print(key + ': ' ,kwargs[key] , end=' ') # these are the two ways to access the key and values in dictionary
        print(key+' : '+str(value), end='')
    
kwargs(name='soorya', age=21, student=True)