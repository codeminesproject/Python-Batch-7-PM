
list_var = [100,200,300,400,500]

print("value of list_var:",list_var)
print("total no of values:",len(list_var))

print("---- remove last value from list ------------")

list_var.pop()

print("value of list_var:",list_var)
print("total no of values:",len(list_var))

print("---- remove value from 2nd position list ------------")

list_var.pop(2)

print("value of list_var:",list_var)
print("total no of values:",len(list_var))

print("---- remove value 100 from list ------------")

list_var.remove(100)

print("value of list_var:",list_var)
print("total no of values:",len(list_var))

print("---- remove all values from list ------------")

list_var.clear()

print("value of list_var:",list_var)
print("total no of values:",len(list_var))