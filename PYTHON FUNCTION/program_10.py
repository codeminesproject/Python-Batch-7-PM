
# return is a keuword used to return value from function

def addition(num_1,num_2):
    add = num_1 + num_2
    print("addition:",add)
    return add
    

def subtraction(num_1,num_2):
    sub = num_2 - num_1
    print("subtraction:",sub)
    return sub

result=addition(25,50)
sub_result=subtraction(result,100)
print("Subtraction:",sub_result)