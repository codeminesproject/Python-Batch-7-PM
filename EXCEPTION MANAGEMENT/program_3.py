
import arithmatic

try:
    

    num_1 = int(input("Please enter num 1: "))
    num_2 = int(input("Please enter num 2: "))

    arithmatic.other()

    add = num_1 + num_2
    print("addition:",add)

    div = num_1 / num_2
    print("division:",div)

    sub = num_1 - num_2
    print("subtraction:",sub)

    mul = num_1 * num_2
    print("multiplication:",mul)
except ValueError as e:
    print(f"Value Error Occured at line no {e.__traceback__.tb_lineno} with message {e}")
except ZeroDivisionError as e:
    print(f"Zero Division Error Occured at line no {e.__traceback__.tb_lineno} with message {e}")
except Exception as e:
    print("Error Line:",e.__traceback__.tb_lineno)
    print("Error Message:",e)
    print("Error Type:",type(e).__name__)

print("program completed")