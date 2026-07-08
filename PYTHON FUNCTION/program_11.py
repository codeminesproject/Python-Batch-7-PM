
def addition(num_1,num_2):
    result = num_1 + num_2
    return result

def subtraction(num_1,num_2):
    result = num_1 - num_2
    return result

def multiplication(num_1,num_2):
    result = num_1 * num_2
    return result

def arithmatic(a,b,selection):
    if selection==1:
        result = addition(a,b)
    elif selection==2:
        result = subtraction(a,b)
    elif selection==3:
        result = multiplication(a,b)
    else:
        result = "Invalid Selection"
    print(result)

num_1 = int(input("Please enter num 1: "))
num_2 = int(input("Please enter num 2: "))
selection = int(input("Please enter 1 for addition. 2 for subtraction, 3 for multiplication: "))

arithmatic(num_1,num_2,selection)
