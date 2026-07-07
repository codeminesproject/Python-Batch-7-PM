# Nested Function: Call One Function into another

def addition():
    num_1 = 100
    num_2 = 200
    add = num_1 + num_2
    print("Addition:",add)
    multiplication()

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
