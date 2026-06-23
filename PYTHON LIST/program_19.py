# prepare list using for while loop:

list_var = []

print("value of list_var:",list_var)
print("no of values in list_var:",len(list_var))

isContinue = "yes"

while isContinue=="yes":
    val = int(input("Please enter value: "))
    list_var.append(val)
    isContinue = input("do you want to continue? press yes else press anything..: ")

print(list_var)