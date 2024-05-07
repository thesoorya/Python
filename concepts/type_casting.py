# Type casting in Python refers to the process of converting a variable from one data type to another. Python provides built-in functions to perform type casting

# String to integer
str_num = "10"
int_num = int(str_num)
print(int_num)

# Float to integer 
float_num = 3.9
int_num = int(float_num)
print(int_num)

# String to float
str_num = "3.14"
float_num = float(str_num)
print(float_num)

# Integer to float
int_num = 10
float_num = float(int_num)
print(float_num)

# Integer to string
int_num = 123
str_num = str(int_num)
print(str_num)

# Float to string
float_num = 3.14
str_num = str(float_num)
print(str_num)

# Integer to boolean (0 becomes False, non-zero becomes True)
bool_val = bool(0)
print(bool_val)

bool_val = bool(9)
print(bool_val)

# String to boolean ("False", "0", empty string become False; others become True)
bool_val = bool("False")
print(bool_val) 

bool_val = bool("")
print(bool_val)  