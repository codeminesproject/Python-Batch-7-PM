
try:
    num_1 = int(input("Please enter num 1: "))
    num_2 = int(input("Please enter num 2: "))

    if num_1==0:
        raise ValueError("num_1 should not be zero")

    if num_2==0:
        raise AttributeError("num_2 should not be zero")

    add = num_1 + num_2
    print("addition:",add)

    div = num_1 / num_2
    print("division:",div)

    sub = num_1 - num_2
    print("subtraction:",sub)

    mul = num_1 * num_2
    print("multiplication:",mul)
finally:
    print("test")

