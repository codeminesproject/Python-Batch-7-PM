
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
    print("Error Line:",e.__traceback__.tb_lineno)
    print("Error Message:",e)
    print("Error Type:",type(e).__name__)