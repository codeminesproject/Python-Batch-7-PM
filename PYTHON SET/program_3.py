
set_var = {10,20,30,40}

print("values of set:",set_var)
print("no of values in set:",len(set_var))

print("----- add 101 in a set ------------")

set_var.add(101)

print("values of set:",set_var)
print("no of values in set:",len(set_var))

print("----- add 99 in a set ------------")

set_var.add(99)

print("values of set:",set_var)
print("no of values in set:",len(set_var))

print("----- add 111,222,333 in a set ------------")

set_var.update([111,222,333])
print("values of set:",set_var)
print("no of values in set:",len(set_var))