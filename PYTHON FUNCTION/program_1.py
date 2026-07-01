
# function: It is a collection of statements
'''
Syntax for function creation:

def function_name():
    logic

def -  def is keyword. you can create function using def keyword

to execute function we have to call function using function name

Types of function:
1. Pre defined function
2. User defined function

1. Pre defined function - print(),input(),min().max(),sum(),len()
2. User defined function - function defined according to user requirement

Rules for function name:
1. Function Name always start from alpha character (a to z)
2. Function name should not contains any special character except underscore _
3. Function name should not start from number
4. Function name should not be a keywords (if, for, while, else elif) or pre defined funtion name
5. Function name can be combination of alpha character (a to z), number and underscore

Sub Types of function:
1. Function With Zero Parameter
2. Function With Parameter
3. Function with return statement
4. lambda function
5. recursive function

'''
#1. Function With Zero Parameter

def addition():
    num_1 = 100
    num_2 = 200
    add = num_1 + num_2
    print("Addition:",add)

def subtraction():
    num_3 = 500
    num_4 = 250
    sub = num_3 - num_4
    print("Subtraction:",sub)

def multiplication():
    num_5 = 5
    num_6 = 25
    mul = num_5 * num_6
    print("Multiplication:",mul)

addition()
multiplication()
addition()
subtraction()