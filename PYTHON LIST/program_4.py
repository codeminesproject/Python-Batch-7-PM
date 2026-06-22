
list_var = [100,200,300,400]

print("value at 0 position:",list_var[0])
print("value at 1 position:",list_var[1])
print("value at 2 position:",list_var[2])
print("value at 3 position:",list_var[3])

print("======= display values of list using for loop =============")

for i in range(0,len(list_var)):
    print(f"value at {i} position: {list_var[i]}")

print("======= display values of list using for each loop =============")

for val in list_var:
    print(val)