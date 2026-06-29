# A dictionary in Python is a mutable, unordered collection that stores key-value pairs.

"""
Syntax:

variable_name = {"key":"value","key":"value","key":"value"}
"""

dict_var = {"id":1,"name":"Veena","percentage":89.98}

print(dict_var)
print("no of key value pair in dictionary:",len(dict_var))
print("datatype of dict_var:",type(dict_var))

print("value of key id:",dict_var["id"])
print("value of key name:",dict_var["name"])
print("value of key percentage:",dict_var["percentage"])

print("---- get all keys from dictionary -----")

for key in dict_var.keys():
    print(key)

print("--- get all values from dictionary ------")

for val in dict_var.values():
    print(val) 

print("--- get all values based on key -----")

for key in dict_var.keys():
    print(f"value of {key} is {dict_var[key]}")

print("--- get all key value pair ---")

for item in dict_var.items():
    print(item)