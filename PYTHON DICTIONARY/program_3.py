
dict_var = {"id":1,"name":"Veena","percentage":89.98,"address":"Ulhasnagar","gender":"female"}

print("values of dict_var:",dict_var)
print("no of key value pair in dictionary:",len(dict_var))

print("--- remove key percentage from dictionary ---")

dict_var.pop("percentage")
print("values of dict_var:",dict_var)
print("no of key value pair in dictionary:",len(dict_var))

print("--- remove key id from dictionary ---")

del dict_var["id"]
print("values of dict_var:",dict_var)
print("no of key value pair in dictionary:",len(dict_var))

print("--- remove last key value pair from dictionary ---")

dict_var.popitem()
print("values of dict_var:",dict_var)
print("no of key value pair in dictionary:",len(dict_var))

