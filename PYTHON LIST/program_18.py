
# prepare list using for loop:

list_var = []

print("value of list_var:",list_var)
print("no of values in list_var:",len(list_var))

size = int(input("Please enter size of list: "))

for i in range(0,size):
    val = int(input("Please enter value: "))
    list_var.append(val)

print("value of list:",list_var)