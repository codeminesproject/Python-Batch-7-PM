
first_num = int(input("Please enter num 1: "))
second_num = int(input("Please enter num 2: "))

operator = int(input("Press 1 -> Addition, 2-> Subtraction, 3 -> Division, 4 -> Multiplication: "))

if operator==1:
    result = first_num + second_num
    print("addition:",result)
elif operator==2:
    result = first_num - second_num
    print("subtraction:",result)
elif operator==3:
    result = first_num / second_num
    print("division:",result)
elif operator==4:
    result = first_num * second_num
    print("multiplication:",result)
else:
    print("Invalid")