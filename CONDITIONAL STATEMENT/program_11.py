
"""

Accept two numbers from user and check
1. both numbers should be greater than 0
2. if yes then only compare two number (equal, greater or smaller)
3. if no then find exactily number which is less than 0

"""

num_1 = -120
num_2 = 100

if num_1>0 and num_2>0:
    if num_1 < num_2:
        print("num 1 is smaller than num 2")
    elif num_1 > num_2:
        print("num 1 is greater than num 2")
    else:
        print("num 1 and num 2 are equal")
else:
    if num_1<=0:
        print("num 1 is less than or equal to 0")
    
    if num_2<=0:
        print("num 2 is less than or equal to 0")