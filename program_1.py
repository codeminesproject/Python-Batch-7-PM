

import sys
# sys means system it is used to show size of datatype

# type(variable) - type is a class used to show datatype of variable

name = "CodeMines"
print(name)
print(type(name)) # <class 'str'> means string
print(sys.getsizeof(name))

print("------------------------------------------------------------------")

age = 19
print(age)
print(type(age)) # <class 'int'> means int
print(sys.getsizeof(age))

print("------------------------------------------------------------------")

percentage = 45.67
print(percentage)
print(type(percentage)) # <class 'float'> means float
print(sys.getsizeof(percentage))