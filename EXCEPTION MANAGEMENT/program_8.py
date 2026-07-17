
try:
    num_1 = int(input("Please enter num 1: "))
    num_2 = int(input("Please enter num 2: "))

    add = num_1 + num_2
    print("addition:",add)

    div = num_1 / num_2
    print("division:",div)

    sub = num_1 - num_2
    print("subtraction:",sub)

    mul = num_1 * num_2
    print("multiplication:",mul)
except Exception as e:
    message = "----------------------------------------------------\n"
    message += "Error Line: "+ str(e.__traceback__.tb_lineno)+"\n"
    message += "Error Message: "+ str(e)+"\n"
    message += "Error Type: "+type(e).__name__+"\n"
    message += "------------------------------------------------------"
    with open("LOGS/error.txt","a") as file:
        file.write(message)
    print("Something went wrong! Please try again")

