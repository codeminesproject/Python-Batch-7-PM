
try:
    num_1 = int(input("Please enter num 1: "))
    num_2 = int(input("Please enter num 2: "))
except Exception as e:
    print("Error Line:",e.__traceback__.tb_lineno)
    print("Error Message:",e)
    print("Error Type:",type(e).__name__)

try:
    add = num_1 + num_2
    print("addition:",add)
except Exception as e:
    print("Error Line:",e.__traceback__.tb_lineno)
    print("Error Message:",e)
    print("Error Type:",type(e).__name__)

try:
    div = num_1 / num_2
    print("division:",div)
except Exception as e:
    print("Error Line:",e.__traceback__.tb_lineno)
    print("Error Message:",e)
    print("Error Type:",type(e).__name__)

try:
    sub = num_1 - num_2
    print("subtraction:",sub)
except Exception as e:
    print("Error Line:",e.__traceback__.tb_lineno)
    print("Error Message:",e)
    print("Error Type:",type(e).__name__)

try:   
    mul = num_1 * num_2
    print("multiplication:",mul)
except Exception as e:
    print("Error Line:",e.__traceback__.tb_lineno)
    print("Error Message:",e)
    print("Error Type:",type(e).__name__)