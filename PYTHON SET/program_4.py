
set_var = {10,20,30,40,111,222,333}

print("values of set:",set_var)
print("no of values in set:",len(set_var))

print("---- remove random value from set ----")

set_var.pop()
print("values of set:",set_var)
print("no of values in set:",len(set_var))

print("---- remove value 30 from set ----")

set_var.remove(30)
print("values of set:",set_var)
print("no of values in set:",len(set_var))

# print("---- remove value 999 from set ----")

# set_var.remove(999)
# print("values of set:",set_var)
# print("no of values in set:",len(set_var))

print("---- discard value 111 from set ----")

set_var.discard(111)
print("values of set:",set_var)
print("no of values in set:",len(set_var))

print("---- discard value 999 from set ----")

set_var.discard(999)
print("values of set:",set_var)
print("no of values in set:",len(set_var))

print("---- remove all values from set ----")

set_var.clear()
print("values of set:",set_var)
print("no of values in set:",len(set_var))