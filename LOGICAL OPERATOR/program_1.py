
# If all three numbers are greater than 0 then numbers are valid otherwise invalid

num_1 = int(input("Please enter num_1: "))
num_2 = int(input("Please enter num_2: "))
num_3 = int(input("Please enter num_3: "))

result = num_1 > 0 and num_2 > 0 and num_3 > 0

print("Valid Numbers:",result)