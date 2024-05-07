# Python provides a variety of string methods for manipulating and working with strings. Here are some of the most commonly used string methods:

# 1. **Conversion and Formatting**:
#    - `str.capitalize()`: Returns a copy of the string with the first character capitalized and the rest lowercased.
#    - `str.lower()`: Returns a copy of the string converted to lowercase.
#    - `str.upper()`: Returns a copy of the string converted to uppercase.
#    - `str.title()`: Returns a titlecased version of the string, where words start with an uppercase character and the remaining characters are lowercase.

# 2. **Searching and Replacing**:
#    - `str.count(substring)`: Returns the number of occurrences of a substring in the string.
#    - `str.find(substring)`: Returns the lowest index of the substring in the string (or -1 if not found).
#    - `str.replace(old, new)`: Returns a copy of the string with occurrences of the 'old' substring replaced by the 'new' substring.
#    - `str.startswith(prefix)`: Returns True if the string starts with the specified prefix; otherwise, returns False.
#    - `str.endswith(suffix)`: Returns True if the string ends with the specified suffix; otherwise, returns False.

# 3. **Whitespace Manipulation**:
#    - `str.strip()`: Returns a copy of the string with leading and trailing whitespace removed.
#    - `str.lstrip()`: Returns a copy of the string with leading whitespace removed.
#    - `str.rstrip()`: Returns a copy of the string with trailing whitespace removed.

# 4. **Splitting and Joining**:
#    - `str.split(sep=None, maxsplit=-1)`: Splits the string into a list of substrings using the specified separator (default is whitespace).
#    - `str.join(iterable)`: Concatenates the elements of an iterable (such as a list) into a single string, using the string as a separator.

# 5. **Checking and Validation**:
#    - `str.isalpha()`: Returns True if all characters in the string are alphabetic (a-z or A-Z).
#    - `str.isdigit()`: Returns True if all characters in the string are digits (0-9).
#    - `str.isalnum()`: Returns True if all characters in the string are alphanumeric (a-z, A-Z, or 0-9).
#    - `str.islower()`: Returns True if all characters in the string are lowercase.
#    - `str.isupper()`: Returns True if all characters in the string are uppercase.

# 6. **Formatting**:
#    - `str.format()`: Formats the string with placeholders to insert values into the string.
#    - `str.format_map(mapping)`: Similar to `str.format()`, but uses a mapping (dictionary) to fill in the placeholders.

# These are just some of the commonly used string methods in Python. There are many more available for various purposes.

string = '    I am studying '

print(len(string))

#converstion and formatting
print(string.capitalize()) #capitalize the first word in sentence
print(string.lower()) #makes the sentence into lower case
print(string.upper()) #makes the sentence into upper case
print(string.title()) #capitalize each starting letter of the word in sentence

#whitespace and manipulation
print(string.strip())
print(string.lstrip())
print(string.rstrip())

#checking and validation
print(string.isalnum())
print(string.isalpha())
print(string.islower())
print(string.isdecimal())
print(string.istitle())

#find
print(string.find('s'))
print(string.count('a'))