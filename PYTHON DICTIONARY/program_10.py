
dict_var = {}

print("values of dict_var:",dict_var)
print("no of values of dict_var:",len(dict_var))

key_size = int(input("Please enter key size: "))

for i in range(0,key_size):
    key_name = input("Please enter key: ")

    data_type = int(input("Press 1 for int, 2 for float and press anything for string: "))

    if data_type==1:
        dict_var[key_name] = int(input(f"Please enter value for {key_name}: "))
    elif data_type==2:
        dict_var[key_name] = float(input(f"Please enter value for {key_name}: "))
    else:
        dict_var[key_name] = input(f"Please enter value for {key_name}: ")

print(dict_var)