
int_tuple = (10,20,30,40,50,20)

print("value of tuple:",int_tuple)

print("---- add 100 in tuple --------")

# step 1: convert tuple into list

list_var = list(int_tuple)

print("values of list:",list_var)

# step 2: add 100 in a list

list_var.append(100)

print("values of list after append:",list_var)

# step 3: convert list into tuple

int_tuple = tuple(list_var)
print("values of int_tuple after adding 100:",int_tuple)