
dict_var = {"id":1,"name":"Veena","percentage":89.98,"address":"Ulhasnagar","gender":"female"}

print("values of dict_var:",dict_var)
print("no of key value pair in dictionary:",len(dict_var))

print("--- Type 1: access id and name keys value from dictionary ---")

print("value of key id:",dict_var["id"])
print("value of key name:",dict_var["name"])

# print("value of key name:",dict_var["college"])

print("--- Type 2: access id and name keys value from dictionary ---")

print("value of key id:",dict_var.get("id"))
print("value of key name:",dict_var.get("name"))

print("value of key college:",dict_var.get("college"))
print("value of key college:",dict_var.get("college","key not present"))